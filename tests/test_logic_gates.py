
# Import the logic gate classes from the logic_gates directory
from my_package.logic_gates.and_gate import ANDGate
from my_package.logic_gates.or_gate import ORGate
from my_package.logic_gates.not_gate import NOTGate

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

if __name__ == "__main__":
    test_and_gate()
    test_or_gate()
    test_not_gate()
