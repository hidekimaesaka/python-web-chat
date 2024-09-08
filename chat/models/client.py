from dataclasses import dataclass


@dataclass
class Client:
    id: int
    username: str
    request: object
