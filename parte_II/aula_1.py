# Operadores lógicos

a = True
b = False

print(a, b) # True False
print(a and b) # False
print(a & b) # False

c = a and b
print("'A' e 'B' são iguais é", c)

print(a or b) # True
print(a | b) # True

d = a or b
print("'A' ou 'B' é igual a", d)

print(not a) # False
print(not b) # True

# Operadores relacionais

print(5 > 3) # True
print(5 < 3) # False
print(5 >= 5) # True
print(5 <= 3) # False
print(5 == 3) # False
print(5 != 3) # True