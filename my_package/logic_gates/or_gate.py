# Define a class for the OR gate
class ORGate:
    def __init__(self, label):
        self.label = label

    # Implement the OR gate logic
    def perform_gate_logic(self, input_a, input_b):
        # The OR gate returns True if at least one input is True, otherwise False
        return input_a or input_b
