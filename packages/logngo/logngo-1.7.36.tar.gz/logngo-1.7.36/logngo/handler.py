import logging
import socketio
import traceback
import threading


class SocketIOHandler(logging.Handler):
    def __init__(self, url: str, handshake_path: str, name: str):
        super().__init__()
        self.sio = socketio.Client()
        self.url = url
        self.handshake_path = handshake_path
        self.name = name
        self.channel = "__logngo"
        self._connect()

    def _connect(self):
        try:
            self.sio.connect(url=self.url, socketio_path=self.handshake_path)
        except Exception as e:
            traceback.print_exc()

    def emit(self, record):
        try:
            self.sio.emit(self.channel, {"name": self.name, "record": self.format(record)})
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        self.sio.disconnect()
        super().close()
