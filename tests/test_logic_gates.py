# Import the logic gate classes from the logic_gates directory
from my_package.logic_gates.and_gate import ANDGate
from my_package.logic_gates.or_gate import ORGate
from my_package.logic_gates.not_gate import NOTGate
from my_package.logic_gates.nand_gate import NANDGate
from my_package.logic_gates.nor_gate import NORGate
from my_package.logic_gates.xor_gate import XORGate

def test_and_gate():
    and_gate = ANDGate("AND Gate")
    
    # Test AND gate logic
    and_gate.set_pins()
    and_gate_output = and_gate.get_output()
    
    # Test if AND gate logic works as expected
    assert and_gate_output == and_gate.get_pin_a() and and_gate.get_pin_b()

def test_or_gate():
    or_gate = ORGate("OR Gate")
    
    # Test OR gate logic
    or_gate.set_pins()
    or_gate_output = or_gate.get_output()
    
    # Test if OR gate logic works as expected
    assert or_gate_output == or_gate.get_pin_a() or or_gate.get_pin_b()

def test_not_gate():
    not_gate = NOTGate("NOT Gate")
    
    # Test NOT gate logic
    not_gate.set_pin()
    not_gate_output = not_gate.get_output()
    
    # Test if NOT gate logic works as expected
    assert not_gate_output == not not_gate.get_pin()

def test_nand_gate():
    nand_gate = NANDGate("NAND Gate")
    
    # Test NAND gate logic
    nand_gate.set_pins()
    nand_gate_output = nand_gate.get_output()
    
    # Test if NAND gate logic works as expected
    assert nand_gate_output == not (nand_gate.get_pin_a() and nand_gate.get_pin_b())

def test_nor_gate():
    nor_gate = NORGate("NOR Gate")
    
    # Test NOR gate logic
    nor_gate.set_pins()
    nor_gate_output = nor_gate.get_output()
    
    # Test if NOR gate logic works as expected
    assert nor_gate_output == not (nor_gate.get_pin_a() or nor_gate.get_pin_b())

def test_xor_gate():
    xor_gate = XORGate("XOR Gate")
    
    # Test XOR gate logic
    xor_gate.set_pins()
    xor_gate_output = xor_gate.get_output()
    
    # Test if XOR gate logic works as expected
    # Implement your XOR gate test logic here

if __name__ == "__main__":
    test_and_gate()
    test_or_gate()
    test_not_gate()
    test_nand_gate()
    test_nor_gate()
    test_xor_gate()
