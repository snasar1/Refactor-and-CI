# Import the Connector class from the connector module
from my_package.connector.connector import Connector

# Create some dummy gate classes for testing
class DummyGate:
    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        return self.output

    def set_next_pin(self, source):
        self.output = source.get_output()

def test_connector():
    # Create instances of dummy gates
    gate1 = DummyGate("Gate 1")
    gate2 = DummyGate("Gate 2")

    # Create a connector between the gates
    connector = Connector(gate1, gate2)

    # Test if the connector correctly connects the gates
    assert gate2.get_output() is None  # Output of gate2 should be None before connecting
    connector.get_from().output = 1  # Set output of gate1 to 1
    assert gate2.get_output() == 1  # Output of gate2 should be 1 after connecting

    # Test if the connector returns the correct source and target gates
    assert connector.get_from() == gate1
    assert connector.get_to() == gate2

if __name__ == "__main__":
    test_connector()

