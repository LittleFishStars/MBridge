from queue import Queue
from typing import Any

queue = Queue()


class QueueMessage:
    def __init__(self, topic: str, msg: Any) -> None:
        self.topic = topic
        self.msg = msg
