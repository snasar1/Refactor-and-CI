# Define a class for connectors between logic gates
class Connector:
    def __init__(self, from_gate, to_gate):
        # Initialize the connector with a source gate and a target gate
        self.from_gate = from_gate
        self.to_gate = to_gate
        # Set the source gate's output to be connected to the target gate
        self.to_gate.set_next_pin(self.from_gate.get_output())

    def get_from(self):
        # Get the source gate
        return self.from_gate

    def get_to(self):
        # Get the target gate
        return self.to_gate
