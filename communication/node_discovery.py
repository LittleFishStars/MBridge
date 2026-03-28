import hashlib
import json
import socket
from threading import Thread
from time import sleep

from loguru import logger

from tool.crypto import Crypto
from tool.ipconfig import get_ip
from tool.message_queue import QueueMessage, queue
from tool.typing import Address, VerifyMessage


class NodeDiscovery:
    broadcast_port = 32990
    listen_port = 32991

    def __init__(self) -> None:
        self.ip = get_ip()

        self.pub_key = Crypto().get_public_key()
        self.node_id = Crypto().get_id()

        self.broadcast = BroadcastThread(
            "Broadcast",
            self.node_id,
            (self.ip, self.broadcast_port),
            self.pub_key.decode("utf-8")
        )
        self.listen = ListenThread(
            "Listen",
            self.node_id,
            (self.ip, self.listen_port)
        )

    def run(self) -> None:
        self.broadcast.start()
        self.listen.start()


class BroadcastThread(Thread):
    def __init__(self, threadID, node_id: str, address: Address, pub_key: str) -> None:
        Thread.__init__(self)
        self.threadID = threadID
        self.node_id = node_id
        self.address = address
        self.pub_key = pub_key

        self.broadcast_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.broadcast_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def run(self):
        """定期广播自身信息（节点ID、IP、公钥）"""
        while True:
            msg = VerifyMessage("NodeDiscovery", self.node_id, *self.address)
            self.broadcast_sock.sendto(
                json.dumps(msg._asdict()).encode("utf-8"),
                ("<broadcast>", self.address.port)
            )
            logger.debug(f"Broadcast: {msg}")
            sleep(5)


class ListenThread(Thread):
    def __init__(self, threadID, node_id: str, address: Address) -> None:
        Thread.__init__(self)
        self.threadID = threadID
        self.node_id = node_id
        self.address = address

        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.listen_sock.bind(self.address)

    def run(self):
        """监听其他节点的广播，更新已发现节点列表"""
        while True:
            data, addr = self.listen_sock.recvfrom(65536)
            try:
                msg = VerifyMessage(**json.loads(data.decode("utf-8")))
                if msg.type == "NodeDiscovery" and msg.node_id != self.node_id:
                    # 验证节点合法性（简单校验：公钥哈希=节点ID）
                    pub_key = msg.pub_key.encode("utf-8")
                    check_id = hashlib.sha256(pub_key).hexdigest()
                    if check_id == msg.node_id:
                        # 合法节点，加入队列
                        queue.put(QueueMessage("NodeDiscovery", msg))
                        logger.info(f"NodeDiscovery: {msg}")
                    else:
                        logger.warning(f"IllegalNode: {msg}")
            except Exception as e:
                logger.trace(f"解析发现消息失败：{e}")
