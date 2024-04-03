'''
passwordinput = '1234'
password = input('Diga a seu senha: ')
tentativas = 1
while password != passwordinput and tentativas < 3:
    print(f"senha incorreta, você so tem mais {3 - tentativas} tentativas")
    password = input("Diga sua senha: ")
    tentativas += 1
print("Acesso Liberado")

vinho1 = "Vinho tinto"
vinho2 = "vinho branco"
vinho3 = "Espumante"

print(f"Temos: \n{vinho1}\n{vinho2}\n{vinho3}")
opcao = input("Diga sua escolha: ")
while not (opcao == vinho1 or opcao == vinho2 or opcao == vinho3):
    print("Opção invalida! ")
    print(f"Nós temos:\n{vinho1}\n{vinho2}\n{vinho3}")
    opcao = input("Diga sua ecolha")

### Exercício 01

nota = int(input("Digite sua nota: "))
while(nota<=0 and nota>=10):
    int(input("Digite uma nota certa "))
    print("Nota invalida, tente novamente ")

print(f"Nota correta {nota}")

###Exercício 02

nome = input("Diga o seu nome: ")
while len(nome)<3:
    nome = int(input("Qual seu nome: "))

idade = int(input("Diga a sua idade: "))
while idade > 150:
    print("Idade invalida!!")
    idade = int(input("digite sua idade novamnete!!!"))

salario = int(input("Diga o quanto voce ganha: "))
while not salario > 0:
    int(input("Seu burro, digite novamente: "))

sexo = input("Diga o seu sexo: ")
while not (sexo == "f" or sexo == "m"):
    sexo = input("Insira o sexo f ou m: ")

estadoCivil = input("Qual o seu estado civil? ")
while not (estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d"):
    estadoCivil = input("Digite s, c, v, d")

###Exercício 03

paisA = 80000
paisB = 200000

ano = 0
while paisA < paisB:
    paisA *= 1.03
    paisB *= 1.015
    ano += 1
print(f"Será necessário {ano} anos")

###Exercício 04

tentativa = 0
soma = 0
while tentativa < 5:
    number1 = int(input("Digite um novo número: "))
    soma += number1
    tentativa = tentativa + 1

print(soma)
print(soma/tentativa)

###Exercício 05

number1 = int(input("Digite um número: "))
number2 = int(input("Digite um novo número: "))
intervalo = number1

while intervalo < number2:
    print(intervalo)
    intervalo += 1

###Exercício 06

nomeUsuraio = input("Diga o seu nome: ")
password = input("Crie sua senha: ")

while nomeUsuraio == password:
    print("A senha não pode ser igual o nome de usuario. ")
    nomeUsuraio = input("diga o seu nome: ")
    password = input("crie a sua senha: ")
print(f"Seja bem-vindo {nomeUsuraio}")

###Exercício 07

num = int(input("Diga um número: "))
i = 1
while i < 11:
    print(num*i)
    i+=1

###Exercício 08

a = 1
b = 1
c = 0
indice = 0

while indice <= 10:
    c = a + b
    a = b
    b = c
    indice += 1
    print(c)

###Exercício 09

indice = 0
par = 0
impar = 0
while indice<3:
    numero = int(input("Digite um número: "))
    if numero %2 == 0:
        par += 1
    else:
        impar += 1
    indice += 1
print(f"Pares são {par}")
print(f"impar são {impar}")
'''

###Exercício 10









