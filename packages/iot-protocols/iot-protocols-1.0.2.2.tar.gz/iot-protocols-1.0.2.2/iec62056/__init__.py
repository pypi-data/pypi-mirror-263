from client import SerialClient
from tools import messages, exceptions

def create_client(configuration: dict) -> SerialClient:
    return SerialClient(**configuration)
