# Refactor and CI Project

This is a Python package for logic gates and binary addition, along with CI integration using GitHub Actions.

## Package Structure

The package is organized as follows:

- `my_package`: Main package directory.
    - `logic_gates`: Directory for logic gate classes.
        - `and_gate.py`: Class for the AND gate.
        - `or_gate.py`: Class for the OR gate.
        - `not_gate.py`: Class for the NOT gate.
        - Other gate modules.
    - `connector`: Directory for the connector class.
        - `connector.py`: Class for connectors between logic gates.
- `tests`: Directory for test files.
    - `test_logic_gates.py`: Test cases for logic gates.
    - `test_connector.py`: Test cases for connectors.
    - `test_eight_bit_adder.py`: Test cases for eight-bit addition.
    - `test_nth_bit_adder.py`: Test cases for binary addition of arbitrary length.
- `hw_file.py`: A sample file.

## Logic Gates

The package provides the following logic gates:

- AND Gate
- OR Gate
- NOT Gate
- Additional gates like NAND, NOR, XOR can be added.

## Binary Addition

The package includes functions for binary addition, supporting both eight-bit addition and binary addition of arbitrary length.

## How to Use

1. Import the necessary logic gate classes from `my_package.logic_gates`.

2. Create instances of the gate classes and use their methods to perform logic operations.

3. To perform binary addition, use the provided functions `eight_bit_adder` and `nth_bit_adder`.

## Testing

The `tests` directory contains test cases for various components. You can run the tests locally and also set up CI using GitHub Actions to ensure code quality.

## CI Pipeline

A GitHub Actions workflow is set up for automated code checks. It includes linting with Flake8 and code formatting with Black.

## Additional Gates

To add more logic gates (e.g., NAND, NOR, XOR), follow the structure of the existing logic gates and create new modules for them.


