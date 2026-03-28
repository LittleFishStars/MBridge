from collections import namedtuple

Address = namedtuple(
    "Address",
    ["ip", "port"]
)

VerifyMessage = namedtuple(
    "VerifyMessage",
    ["type", "node_id", "ip", "pub_key"]
)
