# Rule Engine with AST

This repository contains a Python-based rule engine that uses an Abstract Syntax Tree (AST) to evaluate complex logical expressions. It allows you to define rules in a string format and then parse them into an AST for evaluation.

## Features

- Define rules using logical operators (`AND`, `OR`) and conditions on attributes (e.g., `age > 30`, `department = 'Sales'`).
- Parse rule strings into an AST structure using a custom-built parser.
- Evaluate rules based on dynamic data inputs.
- Easily extendable for more complex operations or conditions.

## Project Structure

- **Node Class**: Represents nodes in the AST. Each node can be an operator (`AND`, `OR`) or an operand (a condition to be evaluated).
- **Rule Parser**: Converts a rule string into an AST, splitting it into operators and operands.
- **Evaluation Logic**: Traverses the AST and evaluates the rule based on the input data.

## Example Usage

### Rule Definition

python
rule = "age > 30 AND department = 'Sales'"

### AST Creation

python
root = create_rule(rule)

### Rule Evaluation

You can extend this rule engine to evaluate rules using input data. For example:

python
data = {'age': 35, 'department': 'Sales'}
result = evaluate_rule(root, data)

This example will parse the rule `"age > 30 AND department = 'Sales'"` and check it against the input data.

## Requirements

- Python 3.x

## Setup

1. Clone the repository:

   git clone https://github.com/kalithasanks2001/Rule-Engine-with-AST.git

2. Navigate into the project directory:

   cd Rule-Engine-with-AST

3. Run the script with your rule input:

   Python: Rule Engine with AST.py

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the rule engine.
