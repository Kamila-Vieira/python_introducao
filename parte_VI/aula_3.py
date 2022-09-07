# Módulos personalizados

import utilitarios as ut

soma = ut.soma(1, 2, 3)
soma2 = ut.soma(1, 2)
print(soma)
print(soma2)

mult = ut.mult(3, 2, 2)
mult2 = ut.mult(3, 2)
print(mult)
print(mult2)

palindromo = ut.isPalindromo('abc')
palindromo2 = ut.isPalindromo('abccba')
print(palindromo)
print(palindromo2)

t = 'abccba'
t2 = 'abc'
print(t[::-1])
print(t2[::-1])

div = ut.divisao(10,2)
print(div)