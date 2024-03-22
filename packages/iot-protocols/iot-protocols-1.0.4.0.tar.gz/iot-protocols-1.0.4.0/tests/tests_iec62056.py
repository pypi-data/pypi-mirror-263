import logging
import time
import pytest
from py_iec62056.client import SerialClient, TariffResponse, messages


@pytest.fixture
def client() -> SerialClient:
    return SerialClient(
        baudrate=19200,
        port="COM3",
        transport="serial",
        parity="E",
        bytesize=7,
        stopbits=1
    )


def test_client_identification(client: SerialClient):
    result = client.read_tariff_identification("5987893", ack_stop=True)
    logging.info(result)
    assert isinstance(result, messages.IdentificationMessage)

    logging.info(f"----- Next Step ----")

    result = client.request(meter_address="5987893", table=7, timeout=3)
    assert isinstance(result, TariffResponse)
    for dataset in result.data:
        logging.info(f"{dataset}")