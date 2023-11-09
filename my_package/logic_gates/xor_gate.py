# Import the new gate classes
from my_package.logic_gates.nand_gate import NANDGate
from my_package.logic_gates.nor_gate import NORGate
from my_package.logic_gates.xor_gate import XORGate

# xor_gate.py

class XORGate:
    def __init__(self, label):
        self.label = label

    def perform_gate_logic(self, input_a, input_b):
        # Implement XOR gate logic
        return (input_a or input_b) and not (input_a and input_b)
      
