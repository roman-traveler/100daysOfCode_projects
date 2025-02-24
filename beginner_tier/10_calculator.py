def operation(a, op, b):
    match op:
        case "+":
            val = a + b
        case "-":
            val = a - b
        case "*":
            val = a * b
        case "/":
            val = a / b
    print(f"{a} {op} {b} = {val}")
    return val


first_number = None
keep_number = False
while True:
    first_number = (
        float(input("Pick first number\n")) if not keep_number else first_number
    )
    op = input("Pick operation: + - * /")
    second_number = float(input("Pick second number\n"))
    first_number = operation(first_number, op, second_number)
    keep_number = (
        input(
            f"Type y to continue calculating with {first_number} or n for anything else\n"
        ).lower()
        == "y"
    )
