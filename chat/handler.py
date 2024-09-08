from chat.models.client import Client

from chat.protocol import Protocol


class ChatHandler(Protocol):
    clients = {}

    def setup(self) -> None:
        id = self._get_id()
        data = self._recv(1024)
        message = self._get_message(data)
        username = self._get_username(message)
        self.clients[id] = Client(id, username, self.request)
        self.broadcast(data)

    def handle(self) -> None:
        while True:
            data = self._recv(1024)
            message = self._get_message(data)
            if not message:
                break
            self._log_message(message)
            self.broadcast(data)

    def _recv(self, length: int) -> bytes:
        return self.request.recv(length).strip()

    def broadcast(self, msg: bytes) -> None:
        for client in self.clients.values():
            if client.request != self.request:
                client.request.sendall(msg)
