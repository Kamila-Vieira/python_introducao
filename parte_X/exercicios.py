""" 1. Crie uma classe chamada aluno com os seguintes atributos:
- Nome
- Nota 1
- Nota 2
- Crie um construtor para a classe (__init__) """

""" 2.Crie as seguintes funções (métodos):
- Calcula média, retornando a média aritmética entre as notas
- Mostra dados, que somente imprime o valor de todos os atributos
- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado) """

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostra_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        print(f'Média: {self.media}')

    def resultado(self):
        if self.media >= 6.0:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')

# 3. Crie dois objetos (aluno1 e aluno2) e teste as funções

aluno1 = Aluno('Pedro', 7.0, 9.0)
aluno1.calcula_media()
aluno1.mostra_dados()
aluno1.resultado()

aluno2 = Aluno('Paula', 5.0, 3.0)
aluno2.calcula_media()
aluno2.mostra_dados()
aluno2.resultado()

