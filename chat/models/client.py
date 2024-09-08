class Client:

    id: int
    username: str
    request: object

    def __init__(self, id: int, request: object) -> None:
        self.id = id
        self.request = request

    def set_username(self, username: str) -> None:
        self.username = username
