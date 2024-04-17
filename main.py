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

while True:
    num = input("Diga um número entre 0 e 10: ")
    if num.isnumeric():
        num = int(num)
        if num>= 0 and num <= 10:
            break
        else:
            print("Deve ser entre 0 e 10")
    else:
        print("mano, ce nem digitou um número, pô")

###Exercício 02

nome = input("Diga o seu nome: ")
while len(nome)<3:
    print('Deve ter no minimo 3 caracteres')
    nome = int(input("Qual seu nome: "))
    
while True:
    num = input("Diga um número entre 0 e 150: ")
    if num.isnumeric():
        num = int(num)
        if num <= 150:
            break
        else:
            print("Deve ser entre 0 e 150")
    else:
        print("mano, ce nem digitou um número, pô")


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
    number1 = input(f"Digite o {tentativa+1}° número: ")
    while not number1.isnumeric():
        print("Deve ser um número!")
        number1 = input(f"Diga o {tentativa+1}°")
    soma += int(number1)
    tentativa += 1


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





i = 1
j = 1
while i <= 10:
    while j <= 10:
        print(f"{i} * {j} = {i*j} ")
        j += 1
    i += 1
    j = 0

    print("\n")


###Exercício 10

num = 5
fatorial = num
fatorial_print = f'{num}! = '
while num > 1:
    fatorial_print += f"{num}*"
    num -= 1
    fatorial *= num
fatorial_print += '1'

print(f"{fatorial_print} = {fatorial}")



###Exercício 11

num = 31
i = 2
while i < num ** 0.5:
    print(f"{num}%{i} = {num%i}")
    if num % i == 0:
        print(f"Não é primo!")
        break
    i += 1
if i >= num ** 0.5:
    print(f"{num} É primo")


###Exercício
final = 2000
salario = 1000
taxa = 0.015
partida = 1995
while partida < final:
    salario *= (1+taxa)
    taxa *= 2
    partida += 1
print(salario)


###Exercício 14
primeiro = 0
segundo = 0
terceiro = 0
quarto = 0

while True:
    num = int(input("Diga um número: "))
    if num < 0:
        break
    if num <= 25:
        primeiro += 1
    elif num <= 50:
        segundo += 1
    elif num <= 75:
        terceiro += 1
    elif num <= 100:
        quarto += 1
 '''

###Exercício 15
joao = 0
jose = 0
jorel = 0
joana = 0
nulo = 0
branco = 0
while True:
    num = input("Diga seu voto: \n 1 - João\n2 - José\n3 - Jorel\n4 - Joana\n5 - Nulo\n6 - Branco\n0 - Sair")
    while num != '0' and num != '1' and num != '2' and num != '3' and num != '4' and num != '5' and num != '6':
        num = input("Diga seu voto:\n 1 - João\n - José\n3 - Jorel\n4 - Joana\n5 - Nulo\n6 - Branco\n0 - Sair")

    if num == '0':
        break
    elif num == '1':
         joao += 1
    elif num == '2':
         jose += 1
    elif num == '3':
         jorel += 1
    elif num == '4':
         joana += 1
    elif num == '5':
         nulo += 1
    elif num == '6':
         branco += 1
    i += 1
print(f"João: {joao}\nJosé: {jose}\nJorel: {jorel}\nJoana: {joana}\nNulo: {nulo}\nBranco: {branco}")
