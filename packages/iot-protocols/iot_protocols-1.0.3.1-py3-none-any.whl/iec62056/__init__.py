from iec62056.client import SerialClient
from iec62056.tools import messages, exceptions

def create_client(configuration: dict) -> SerialClient:
    return SerialClient(**configuration)
