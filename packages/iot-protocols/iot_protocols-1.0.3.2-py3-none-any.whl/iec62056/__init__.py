from iec62056.client import SerialClient
from iec62056 import tools

def create_client(configuration: dict) -> SerialClient:
    return SerialClient(**configuration)
