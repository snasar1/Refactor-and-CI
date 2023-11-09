# Define a class for the NOT gate
class NOTGate:
    def __init__(self, label):
        self.label = label

    # Implement the NOT gate logic
    def perform_gate_logic(self, input_a):
        # The NOT gate returns the opposite of the input (True becomes False, and vice versa)
        return not input_a
