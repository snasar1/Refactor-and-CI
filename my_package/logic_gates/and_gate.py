# Define a class for the AND gate
class ANDGate:
    def __init__(self, label):
        self.label = label

    # Implement the AND gate logic
    def perform_gate_logic(self, input_a, input_b):
        # The AND gate returns True if both inputs are True, otherwise False
        return input_a and input_b
