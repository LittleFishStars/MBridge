from communication.node_discovery import NodeDiscovery
from tool.typing import Address


class ConnectionManager:
    def __init__(self) -> None:
        self.discovery_manager = NodeDiscovery()
        self.discovery_manager.run()


class Connection:
    def __init__(self, address: Address) -> None:
        pass
