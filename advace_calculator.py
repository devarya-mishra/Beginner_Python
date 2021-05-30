logo = """
 _____________________
|  _________________  |
| |    Calculator   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

# Calculater

# Adding
def add(n1, n2):
    op = n1 + n2
    return op

# Substracting
def substract(n1, n2):
    op = n1 - n2
    return op

# Multiply
def multiply(n1, n2):
    op = n1 * n2
    return op

# Divide
def divide(n1, n2):
    op = n1 / n2
    return op

operation = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}
def calculator():
    not_end = True
    num1 = int(input("Enter your number: "))
    for i in operation:
        print(i)
    while not_end:
        operation_symbol = input("Pick an operation: ")        
        num2 = int(input("Enter your next number: "))
        calc = operation[operation_symbol]
        ans = calc(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {ans}')

        if input("Enter y to continue and n to restart: ") == 'y':
                num1 = ans
        else:
            print("Something went wrong!")
calculator()