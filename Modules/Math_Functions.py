def sum(n1, n2):

    print(f"The sum is: {n1 + n2}");

def substract(n1, n2):

    print(f"The substract is {n1 - n2}")

def multiply(n1, n2):

    print(f"The multiplication is: {n1 * n2}")

def divide(n1, n2):

    try:
    
        op = n1/n2

        print(f"The division is: {op}")

    except ZeroDivisionError:
        print("Operación errónea");