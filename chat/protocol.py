from socketserver import BaseRequestHandler

from json import JSONDecodeError, loads

from chat.errors.invalid_request import InvalidRequestError

from chat.models.message import Message


class Protocol(BaseRequestHandler):

    def _get_id(self):
        return self.client_address[1]

    def _get_username(self, message: Message) -> str:
        return message.username

    def _get_message(self, data: bytes) -> Message:
        try:
            str_json = data.decode()
            json = loads(str_json)
            return Message(**json)
        except JSONDecodeError:
            print(InvalidRequestError.message)

    def _log_message(self, message: Message) -> None:
        print(message)
