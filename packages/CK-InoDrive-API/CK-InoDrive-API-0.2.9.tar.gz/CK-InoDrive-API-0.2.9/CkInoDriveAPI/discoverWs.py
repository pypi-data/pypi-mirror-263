import logging

from .defines import CK
from .utils import Utils
from .wsHandle import InoDriveWS


class DiscoverWs(object):
    def __init__(self, **kwargs):
        self._connection_handle: InoDriveWS = kwargs.get('connection_handle')

    def dispose(self):
        return

    def get_info(self):
        try:
            # Send request and wait for response
            resp = self._connection_handle.request(Utils.get_tlv(CK.SPECIAL.GET_DISCOVER_INFO))

            if resp.get('error'):
                logging.error(f'Retrieving discover info failed...')
                return None

            result = None

            resp_items = resp.get('items')
            if resp_items and len(resp_items) > 0:
                data = resp_items[0].get('data')

                # Discover version
                # =======================================================================
                item_size = 1
                discover_version = Utils.get_typed_value(data[0:item_size], 'uint8')
                data = data[item_size:]
                # =======================================================================

                # SN
                # =======================================================================
                item_size = 25
                sn = Utils.get_typed_value(data[0:item_size], 'string')
                data = data[item_size:]
                # =======================================================================

                # PN
                # =======================================================================
                item_size = 25
                pn = Utils.get_typed_value(data[0:item_size], 'string')
                data = data[item_size:]
                # =======================================================================

                # Name
                # =======================================================================
                item_size = 33
                name = Utils.get_typed_value(data[0:item_size], 'string')
                data = data[item_size:]
                # =======================================================================

                # Firmware version
                # =======================================================================
                item_size = 1
                fw_major = Utils.get_typed_value(data[0:item_size], 'uint8')
                data = data[item_size:]

                item_size = 1
                fw_minor = Utils.get_typed_value(data[0:item_size], 'uint8')
                data = data[item_size:]

                item_size = 1
                fw_build = Utils.get_typed_value(data[0:item_size], 'uint8')
                data = data[item_size:]

                item_size = 1
                fw_type = Utils.get_typed_value(data[0:item_size], 'uint8')
                data = data[item_size:]

                firmware_flags = Utils.get_firmware_flags(fw_type)
                # =======================================================================

                # Networking
                # =======================================================================
                item_size = 6
                mac_address = Utils.get_typed_value(data[0:item_size], 'macAddress')
                data = data[item_size:]

                item_size = 4
                ip_address = Utils.get_typed_value(data[0:item_size], 'ipV4')
                data = data[item_size:]

                item_size = 4
                net_mask = Utils.get_typed_value(data[0:item_size], 'ipV4')
                data = data[item_size:]

                item_size = 4
                gateway = Utils.get_typed_value(data[0:item_size], 'ipV4')
                data = data[item_size:]

                item_size = 4
                dns = Utils.get_typed_value(data[0:item_size], 'ipV4')
                data = data[item_size:]
                # =======================================================================

                # PCB Version
                # =======================================================================
                pcb_major = 1
                pcb_minor = 1
                pcb_build = 1
                pcb_type = 0

                if discover_version >= 2:
                    item_size = 1
                    pcb_major = Utils.get_typed_value(data[0:item_size], 'uint8')
                    data = data[item_size:]

                    item_size = 1
                    pcb_minor = Utils.get_typed_value(data[0:item_size], 'uint8')
                    data = data[item_size:]

                    item_size = 1
                    pcb_build = Utils.get_typed_value(data[0:item_size], 'uint8')
                    data = data[item_size:]

                    if discover_version >= 3:
                        item_size = 1
                        pcb_type = Utils.get_typed_value(data[0:item_size], 'uint8')
                        data = data[item_size:]

                pcb_flags = Utils.get_pcb_flags(pcb_type)
                # =======================================================================

                result = {
                    'discoverVersion': discover_version,
                    'sn': sn,
                    'pn': pn,
                    'name': name,
                    'firmware': '.'.join([str(fw_major), str(fw_minor), str(fw_build)]),
                    'firmwareFlags': firmware_flags,
                    'network': {
                        'ip': ip_address,
                        'mask': net_mask,
                        'gw': gateway,
                        'dns': dns,
                        'mac': mac_address,
                    },
                    'pcb': '.'.join([str(pcb_major), str(pcb_minor), str(pcb_build)]),
                    'pcbFlags': pcb_flags
                }

            return result
        except Exception as ex:
            logging.exception(ex)

        return None
