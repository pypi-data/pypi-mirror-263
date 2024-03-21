import re
import time
import logging
import datetime
import threading
import websocket

from .defines import CK
from .utils import Utils


class InoDriveWS(object):
    def __init__(self, **kwargs):

        # Target module network identifier: IP Address, SN, Name
        self._target = kwargs.get('target')
        if type(self._target) != str:
            raise Exception(f'Target device not provided...')
        self._port = kwargs.get('port')
        # Api path - entry point
        self._path = kwargs.get('path', 'cmd')
        # Secure or non-secure WebSocket
        self._secure = True if kwargs.get('secure') else False
        # Other
        self._reconnect_attempts = kwargs.get('reconnectAttempts', 3)
        # Timeout notes:
        # connectTimeout should be 3 - 15 seconds. Low values like 3-5 should be good, even over the internet.
        # socketTimeout should be ~10. When a file transfer overwrites a file, there could be 2-3 seconds of
        # filesystem overhead and the transfer of 300k+ firmware file takes 2+ seconds.
        # Maybe we need separate file transfer and variable API timeouts.
        self._create_timeout = kwargs.get('createTimeout', 15)
        self._connect_timeout = kwargs.get('connectTimeout', 15)
        self._socket_timeout = kwargs.get('socketTimeout', 10)
        self._request_timeout = kwargs.get('requestTimeout', 10)
        self._keep_alive_timeout = kwargs.get('keepAliveTimeout', 5)
        self._reconnect_timeout = kwargs.get('reconnectTimeout', 6)
        # Flags
        self._auto_connect = kwargs.get('autoConnect', False)
        self._reconnect = kwargs.get('reconnect', True)
        self._keep_alive = kwargs.get('keepAlive', True)
        self._binary = kwargs.get('binary', True)
        # Callbacks
        self._callbacks = {
            'onConnect': kwargs.get('onConnect'),
            'onDisconnect': kwargs.get('onDisconnect'),
            'onError': kwargs.get('onConnect'),
            'onMessage': kwargs.get('onMessage')
        }

        if self._keep_alive_timeout < 1:
            self._keep_alive_timeout = 1

        self._target_url = self._get_target_url()

        self._reconnect_count = self._reconnect_attempts

        self._last_request_time = datetime.datetime.now()

        self._msg_queue = {}

        self._msg_send_allowed_timeout = 0.1
        self._msg_send_allowed = True

        self._cmd_state = None
        self._state = 'disconnected'

        self._wsapp = None
        self._ws_thread = None
        self._ws_thread_running = False

        self._connection_guard_timeout = 0.1
        self._connection_guard_timer = None

    def dispose(self):
        try:
            logging.debug(f'Dispose connection -> host [{self._target}]...')
            self._cmd_state = "dispose"

            self.disconnect()

            self._msg_queue = {}

        except Exception as ex:
            logging.error(str(ex))

    def set_target(self, target=None):
        try:
            if type(target) is not str:
                logging.error(f"Target is not string: {target}")
                return
            self._target = target
            self._target_url = self._get_target_url()
        except Exception as ex:
            logging.exception(ex)

    def connected(self):
        return True if self._state == "connected" else False

    def disconnected(self):
        return True if self._state == "disconnected" else False

    def set_binary(self, flag):
        return {}

    def on(self, evt, func):
        try:
            match evt:
                case "connect":
                    self._callbacks['onConnect'] = func if callable(func) else None
                case "disconnect":
                    self._callbacks['onDisconnect'] = func if callable(func) else None
                case "error":
                    self._callbacks['onError'] = func if callable(func) else None
                case "message":
                    self._callbacks['onMessage'] = func if callable(func) else None
        except Exception as ex:
            logging.info(str(ex))

    def connect(self, target=None, timeout=None):
        try:
            if self._state == "connected":
                return True

            if type(target) == str:
                self._target_url = self._target

            self._state = "connecting"
            self._cmd_state = "connect"

            if self._connection_guard_timer is None:
                self._guard_start()

            if not getattr(self, "_wsapp", False):
                logging.warning(f"Connect to: ---> {self._target_url}")
                # WebSocket instance
                self._wsapp = websocket.WebSocketApp(
                    self._target_url,
                    on_open=self.on_connect,
                    on_close=self.on_disconnect,
                    on_error=self.on_error,
                    on_message=self.on_message
                )

            websocket.setdefaulttimeout(self._connect_timeout)
            self._ws_thread = threading.Thread(target=self._wsapp.run_forever, daemon=True)
            self._ws_thread_running = True
            self._ws_thread.start()

            if timeout:
                timeout = timeout
            else:
                timeout = self._connect_timeout

            # Wait for socket to connect or timeout
            timeout_state = False
            while not self.connected() and timeout > 0:
                timeout -= 1
                time.sleep(1)

            if not self.connected():
                timeout_state = True

            if timeout_state:
                logging.error(f"Connecting to: {self._target} timeout...")

            return self.connected()

        except Exception as ex:
            logging.info(str(ex))

        return False

    def disconnect(self, timeout=None):
        try:
            if self._state == "disconnected":
                self._dispose_ws()
                return

            self._state = 'disconnecting'
            self._cmd_state = 'disconnect'
            self._guard_stop()

            # Close Websocket App
            if self._wsapp:
                self._wsapp.close()

            if timeout:
                timeout = timeout
            else:
                timeout = self._connect_timeout

            timeout_state = False
            while not self.disconnected() and timeout > 0:
                timeout -= 1
                time.sleep(1)

            if not self.disconnected():
                timeout_state = True

            if timeout_state:
                logging.error(f"Disconnecting from: {self._target} timeout...")
            else:
                self._dispose_ws()

            return self.disconnected()

        except Exception as ex:
            logging.error(str(ex))

        return False

    def request(self, payload=None, timeout=None, blocking=True):
        try:
            if type(payload) != bytes:
                return {'success': False, 'error': 'Payload is None...'}

            self._last_request_time = datetime.datetime.now()

            token = Utils.get_token(8, bytes=False)

            msg = b''
            msg += Utils.get_tlv(CK.UNIQUE_TOKEN, token)
            msg += payload

            queue_item = {
                'state': "sent",
                'time': self._last_request_time,
                'error': None,
                'response': None,
            }

            if blocking:
                # If we are going to wait for response addi the item to the queue
                self._msg_queue_put(token, queue_item)

            if not self._send(msg):
                # Send failed for some reason
                return {'success': False, 'error': 'Send failed...'}

            # If we are not going to wait for response just return success
            if not blocking:
                return {'success': True}

            if timeout:
                timeout = timeout * 100
            else:
                timeout = self._socket_timeout * 100

            while queue_item['response'] is None and timeout > 0:
                timeout -= 1
                time.sleep(0.01)

            if queue_item['response'] is None and timeout <= 0:
                return {'success': False, 'error': 'timeout'}

            response = queue_item['response']

            # Remove this request item from the queue
            self._msg_queue.pop(token, None)

            return response

        except Exception as ex:
            logging.error(str(ex))
            return {'success': False, 'error': ex}

    def msg_pack_request(self, msg=[]):
        try:
            msg_tlv = Utils.get_msg_pack_tlv(msg)
            response = self.request(msg_tlv)

            if response.get('error'):
                return {
                    'success': False,
                    'error': response['error'],
                }

            if len(response['items']) == 0:
                return {
                    'success': False,
                    'error': 'Response items are missing...'
                }

            if response['items'][0]['ctpType'] != CK.TYPE.MSG_PACK:
                return {
                    'success': False,
                    'error': 'Response item is not MsgPack...'
                }

            msg_pack_data = response['items'][0]['data']

            if len(msg_pack_data) < 2:
                return {
                    'success': False,
                    'error': 'MsgPack returns less then required two items - success and error'
                }

            if not msg_pack_data[0]:
                # todo: Decode the message -> msg_pack_data[1]
                return {
                    'success': False,
                    'error': msg_pack_data[1],
                }

            response_msg = {
                'success': True,
                'token': response.get('token'),
                'data': msg_pack_data[2:],
            }

            if response.get('ntpTime'):
                response_msg.update({'ntpTime': response['ntpTime']})

            return response_msg
        except Exception as ex:
            return {
                'success': False,
                'error': str(ex)
            }

    def on_message(self, wsapp, msg):
        try:
            if self._binary:
                msg = Utils.decode_tlv_message(msg)

            msg_token = None
            if msg.get("token"):
                msg_token = Utils.get_typed_value(msg['token'][0:], 'string')

            msg_request = self._msg_queue_get(msg_token)
            if msg_request:
                msg_request['state'] = "received"
                if msg.get('error'):
                    logging.error(msg['error'])
                    msg_request['error'] = True
                elif msg['response'] != CK.RESULT.OK:
                    result_name = Utils.get_result_name_by_value(msg['response'])
                    logging.error(f"Unexpected response type [{msg['response']}]: {result_name}")
                    msg_request['error'] = True
                else:
                    msg_request['response'] = msg

                self._msg_queue_pull(msg_token)

            if self._callbacks.get('onMessage'):
                self._callbacks['onMessage'](msg)
        except Exception as ex:
            logging.exception(str(ex))

    def on_connect(self, wsapp):
        logging.debug(f'Connection connected: {self._target_url}')

        self._state = "connected"

        if self._callbacks.get('onConnect'):
            self._callbacks['onConnect'](wsapp)

    def on_disconnect(self, wsapp, close_status_code, close_msg):
        logging.debug(f'Connection disconnected: {self._target_url}')

        self._state = "disconnected"

        if self._callbacks.get('onDisconnect'):
            self._callbacks['onDisconnect'](wsapp, close_status_code, close_msg)

    def on_error(self, wsapp, evt):
        logging.exception(f'Connection error: {self._target_url}')

        self._state = "error"

        if self._callbacks.get('onError'):
            self._callbacks['onError'](wsapp, evt)

    def _msg_queue_get(self, token):
        try:
            return self._msg_queue.get(token)
        except Exception as ex:
            pass
        return None

    def _msg_queue_put(self, token, props):
        if token in self._msg_queue:
            # Should never happen
            logging.warning(f'Message with token [ {token} ] already exist...')
            logging.warning(f'Connection message queue [ {token} ] -> Duplicated token...')
            return
        self._msg_queue.update({token: props})

    def _msg_queue_pull(self, token):
        try:
            self._msg_queue.pop(token)
        except Exception as ex:
            pass

    def _get_target_url(self, timestamp=True):
        return Utils.get_target_url(self._target, {'port': self._port, 'path': self._path, 'secure': self._secure, 'timestamp': timestamp})

    def _dispose_ws(self):
        try:
            if self._wsapp:
                self._wsapp.on_open = {}
                self._wsapp.on_close = {}
                self._wsapp.on_error = {}
                self._wsapp.on_message = {}
                self._wsapp = None

            if self._ws_thread:
                self._ws_thread.join()
                self._ws_thread_running = False
                self._ws_thread = None
        except Exception as ex:
            logging.exception(ex)

    def _send(self, data=None):
        try:
            if self.connected():
                self._wsapp.sock.send_binary(data)
                return True
        except Exception as ex:
            logging.error(str(ex))

            return False

    def _send_keep_alive(self):
        self.request(Utils.get_tlv(CK.NOP), blocking=False)

    def _guard_start(self):
        if not self._connection_guard_timer:
            logging.warning(f'Start guard [ {self._target_url} ]')
            self._connection_guard_timer = threading.Thread(target=self._connection_guard_loop, daemon=True)
            self._connection_guard_running = True
            self._connection_guard_timer.start()

    def _guard_stop(self):
        logging.warning(f'Stop guard [ {self._target_url} ]')
        self._connection_guard_running = False
        self._connection_guard_timer.join()
        self._connection_guard_timer = None

    def _connection_guard_loop(self):
        while self._connection_guard_running:
            try:
                if self._cmd_state == "dispose":
                    return

                expire_list = []
                ws_time = datetime.datetime.now()

                # Garbage Collect Message Queues Which Timeout
                # =====================================================================================================
                for token, props in self._msg_queue.items():
                    if props and type(props) == dict:
                        if (ws_time - props['time']) >= datetime.timedelta(seconds=self._request_timeout):
                            props['state'] = "timeout"
                            expire_list.append(token)

                for token in expire_list:
                    logging.warning(f"Connection {self._target_url} token [ {token} ] timeout -> Garbage collected...")
                    if self._msg_queue[token]['error']:
                        logging.error(f"Request ID:{token} timeout...")
                    del self._msg_queue[token]

                # Keep Alive
                # =====================================================================================================
                if self.connected():
                    time_delta = datetime.datetime.now() - self._last_request_time
                    keep_alive_timeout = datetime.timedelta(seconds=self._keep_alive_timeout)
                    if time_delta >= keep_alive_timeout:
                        self._send_keep_alive()

                # Reconnect
                # =====================================================================================================
                if self._reconnect and self._cmd_state == "connect" and self._state == "disconnected":
                    if getattr(self, "_reconnect_time", 0):
                        reconnect_timeout = datetime.timedelta(seconds=self._reconnect_timeout)
                        if (datetime.datetime.now() - self._reconnect_time) >= reconnect_timeout:
                            logging.warning(f"Reconnect to: {self._target}")
                            self._reconnect_time = None

                            self.disconnect()

                            if self._reconnect_count > 0:
                                self._reconnect_count -= 1
                                if self._reconnect_count <= 2:
                                    if self._reconnect_count <= 0:
                                        self._reconnect_count = self._reconnect_attempts
                                        self._target_url = self._get_target_url()
                                        self.connect()
                                    else:
                                        self._target_url = self._get_target_url(timestamp=False)
                                        self.connect()
                    else:
                        self._reconnect_time = datetime.datetime.now()
                        # Unhandled exception - give it some time to recover
                        time.sleep(1)
                time.sleep(self._connection_guard_timeout)
            except Exception as ex:
                logging.error(str(ex))
