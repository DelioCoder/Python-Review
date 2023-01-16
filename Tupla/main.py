mitupla = ("Juan", 13, 1, 1995);

# print(mitupla[2]);

# Convert tupla to list

milista = list(mitupla);

# Convert list to tupla

milista2 = ["Cristiano", 12, 2, 1988, 12];

mitupla2 = tuple(milista2);

# print("Cristiano" in mitupla2)

# print(mitupla2.count(12)) #How many times 12 is in the tupla

# print(len(mitupla2))

tuplauni = ("Juan",)

tuplawp = "Juan", 15, 2, 1994 # <- Empaquetado de Tupla

print(len(tuplauni))

print(tuplawp)

#Desempaquetado de Tuplas

tuplaexample = ("Undertaker", 10, 2, 1955)

nombre, dia, mes, agno = tuplaexample

print(nombre);
print(dia);
print(mes);
print(agno);