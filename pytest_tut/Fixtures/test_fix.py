import pytest
from unittest.mock import Mock

# Mock UART communication class
class MockUART:
    def __init__(self):
        self.data_written = []
        self.data_to_read = []
    
    def write(self, data):
        self.data_written.append(data)
    
    def read(self):
        if self.data_to_read:
            return self.data_to_read.pop(0)
        return None

    def set_read_data(self, data_list):
        self.data_to_read = data_list

# Fixture for initializing mock UART communication
@pytest.fixture
def mock_uart():
    uart = MockUART()
    return uart

# Example tests using the mock_uart fixture
def test_uart_write(mock_uart):
    mock_uart.write("Hello")
    mock_uart.write("World")
    assert mock_uart.data_written == ["Hello", "World"]

def test_uart_read(mock_uart):
    mock_uart.set_read_data(["Data1", "Data2"])
    assert mock_uart.read() == "Data1"
    assert mock_uart.read() == "Data2"
    assert mock_uart.read() is None
