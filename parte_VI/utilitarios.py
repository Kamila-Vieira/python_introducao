def soma(a, b, c = 0):
    produto = a + b + c
    return produto

def mult(a, b, c = 1):
    produto = a * b * c
    return produto

def isPalindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False

def divisao(a, b): 
    produto = a / b
    return produto