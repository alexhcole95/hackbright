"""CLI application for a prefix-notation calculator."""

from arithmetic import (
    add,
    subtract,
    multiply,
    divide,
    square,
    cube,
    power,
    mod,
)

# Replace this with your code
while True:
    user_input = input(">")
    tokens = user_input.split(" ")

    if "q" in tokens:
        break

    result = None
    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = None

    else:
        num2 = tokens[2]

    if operator == "+":
        result = add(float(num1), float(num2))

    if operator == "-":
        result = subtract(float(num1), float(num2))

    if operator == "*":
        result = multiply(float(num1), float(num2))

    if operator == "/":
        result = divide(float(num1), float(num2))

    if operator == "square":
        result = square(float(num1))

    if operator == "cube":
        result = cube(float(num1))

    if operator == "pow":
        result = power(float(num1), float(num2))

    if operator == "mod":
        result = mod(float(num1), float(num2))

    print(result)
