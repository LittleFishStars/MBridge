from queue import Queue
from typing import Any

# 全局消息队列实例
queue = Queue()


class QueueMessage:
    """队列消息类"""
    def __init__(self, topic: str, msg: Any) -> None:
        """初始化队列消息
        
        Args:
            topic: 消息主题
            msg: 消息内容
        """
        self.topic = topic
        self.msg = msg