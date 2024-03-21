import logging
import weakref

from .wsHandle import InoDriveWS
from .file import File
from .discoverWs import DiscoverWs
from .IO import IO
from .sysControl import SysControl
from .userApp import UserApp


class InoDrive(object):
    def __init__(self, **kwargs):
        logging.debug('Create InoDrive instance...')
        self._auto_connect = kwargs.get('autoConnect', False)

        # ==============================================================================================================
        # MODULES BEGIN
        # ==============================================================================================================
        self._connection_handle = InoDriveWS(**kwargs)
        self.File = File(connection_handle=self._connection_handle, **kwargs)
        self.Discover = DiscoverWs(connection_handle=self._connection_handle, **kwargs)
        self.IO = IO(connection_handle=self._connection_handle, **kwargs)
        self.SysControl = SysControl(connection_handle=self._connection_handle, **kwargs)
        self.UserApp = UserApp(connection_handle=self._connection_handle, **kwargs)
        # ==============================================================================================================
        # MODULES END
        # ==============================================================================================================

        # ==============================================================================================================
        # CONNECTION
        # ==============================================================================================================
        self.on = self._connection_handle.on
        self.connected = self._connection_handle.connected
        self.connect = self._connection_handle.connect
        self.disconnect = self._connection_handle.disconnect
        self.set_target = self._connection_handle.set_target
        # ==============================================================================================================
        # CONNECTION END
        # ==============================================================================================================
        
        # Finalizer weak reference to ensure InoDrive Object is cleaned up on code exit
        self._finalizer = weakref.finalize(self, self.dispose)

        if self._auto_connect:
            self._connection_handle.connect()

    def __del__(self):
        self._finalizer()

    def dispose(self):
        if self.UserApp:
            self.UserApp.dispose()

        if self._connection_handle:
            self._connection_handle.dispose()
