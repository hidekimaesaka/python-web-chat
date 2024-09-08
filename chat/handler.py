from json import loads, JSONDecodeError

from socketserver import BaseRequestHandler

from chat.models.client import Client

from chat.errors.invalid_request import InvalidRequestError


class ChatHandler(BaseRequestHandler):

    clients = {}

    def handle(self):
        id = self.client_address[1]
        request = self.request
        client = Client(id, request)

        self.clients[id] = client

        while True:
            request_data = self.request.recv(1024).strip()
            json_data = self.process_request_data(request_data)

            if json_data:
                username = self.get_username(json_data)
                message = self.get_message(json_data)
                client.set_username(username)
                print(f'{client.username}: {message}')
                self.broadcast(request_data)

            break

    def process_request_data(self, request_data: bytes) -> dict:
        try:
            return loads(request_data.decode())

        except JSONDecodeError:
            print(InvalidRequestError.message)

    def get_username(self, json_data: dict) -> str:
        return json_data.get('username')
    
    def get_message(self, json_data: dict) -> str:
        return json_data.get('message')

    def broadcast(self, msg) -> None:
        for client in self.clients.values():
            if client.request != self.request:
                client.request.sendall(msg)
