class NORGate:
    def __init__(self, label):
        self.label = label

    def perform_gate_logic(self, input_a, input_b):
        # Implement NOR gate logic
        return not (input_a or input_b)
