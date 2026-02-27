print('Shrihari')
print("Welcome to the calculator: ")
nexts = ''
result = None  

while True:
    if nexts == 'y' and result is not None:
        a = result
    else:
        a = int(input("Enter the first value: "))
        b = int(input("Enter the second value: "))
 
    operations = input("Enter the operations + - * / %: ").strip()

    if operations == '+':
        result = a + b
    elif operations == '-':
        result = a - b
    elif operations == '*':
        result = a * b
    elif operations == '/':
        try:
            result = a / b
        except ZeroDivisionError:
            print('division by zero')
            continue
    elif operations == '%':
        try:
            result = a % b
        except ZeroDivisionError:
            print('division by zero')
            continue
    else:
        print("Invalid operation. Please choose from + - * / %")
        continue
        
    nexts = input("If you want to continue with the result, type 'y', otherwise 'n': ").lower().strip()
    if nexts == 'n':
        close = input("Type 'q' to quit or 'n' for a new calculation: ").lower().strip()
        print(f'Result: {result}')
        if close == 'q':
            print("Closed the Calculator app")
            break
        else:
            nexts = ''
            continue
    else:
        print(f'Result: {result}')
        continue
