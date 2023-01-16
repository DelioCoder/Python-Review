num_1 = int(input("Introduce un número: "))

lastnum = 0

while num_1 > 0:

    sum = num_1 + lastnum;

    lastnum = sum

    num_1 = int(input("Introduce otro número: "));

print(f"La suma es {lastnum}")