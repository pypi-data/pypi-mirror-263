from dataclasses import dataclass
from typing import List


@dataclass
class NetworkAddress:
    host: str
    port: int


@dataclass
class NetworkConfig:
    edgeServers: List[NetworkAddress]
