from dataclasses import dataclass

from typing import List

from chat.models.data import Data


@dataclass
class Message:
    timestamp: int
    username: str
    data: List[Data]
