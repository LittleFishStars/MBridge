from collections import namedtuple

# 地址命名元组，用于表示网络地址
Address = namedtuple(
    "Address",
    ["ip", "port"]
)

# 节点发现消息命名元组，用于节点间发现
DiscoveryMessage = namedtuple(
    "DiscoveryMessage",
    ["type", "node_id", "ip", "pub_key"]
)

# 验证消息命名元组，用于节点验证
VerifyMessage = namedtuple(
    "VerifyMessage",
    ["type", "fingerprint", "port"]
)