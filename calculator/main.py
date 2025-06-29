def calculate(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    elif z == '%':
        return x % y
    elif z == '**':
        return x ** y
    elif z == '//':
        if y != 0:
            return x // y
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

x = input('Enter first number: ');
y = input('Enter second number: ');
z = input('Enter the operator: ');

result = calculate(float(x), float(y), z)
print(f'The result is: {result}')