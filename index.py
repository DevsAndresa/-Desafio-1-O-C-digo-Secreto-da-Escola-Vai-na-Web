#Missão 1: Restaurando as Regras Escolares 📝 

nota = int(input('Digite a nota do aluno: '))
if nota >= 5:
    print('O aluno está aprovado')
else:
    print('O aluno está reprovado')

#Missão 2: O Sistema Eleitoral Secreto 📝 
idade = int(input('Digite a sua idade: '))
if idade >= 16:
    print('Você pode votar')
else:
    print('Você não pode votar, idade inferior ao mínimo permitido.')

#Missão 3: Recuperando o Sistema de Notas 📊

nota=int(input('Digite a sua nota: '))

if nota>=90:
    print("Parabéns, você tirou A!")
elif nota>=80 and nota<89:
    print("Muito bem, você tirou B.")
elif nota>=70 and nota<79:
    print("Bom trabalho, você tirou C.")
elif nota>=60 and nota<69:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

#MMissão 4: Restaurando a Identificação de Números ⚖️

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


soma = num1 + num2

print(f"A soma de {num1} e {num2} é {soma}")

#Missão 5: Recuperando o Cofre de Segurança 🔒

senha_correta = "Python123"


senha_digitada = input("Digite a senha: ")


if senha_digitada == senha_correta:
    print("Acesso permitido")
else:
    print("Senha incorreta.")

#Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾

dado_inicial= 1

while dado_inicial <= 10:
    print(f'{dado_inicial}')
    dado_inicial+=1

#Missão 7: Organizando a Lista📋

lista_de_numeros = [8, 3, 10, 1 , 5]

lista_de_numeros.sort()

print (lista_de_numeros)


#Missão 8: Acessando os Registros de Alunos 🏷️
alunos = ('Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo')


print(alunos[0])


print(alunos[-1])


#Missão 9: Calculando Dobro de um Número 🛠️

numero = float(input("Digite o número: "))



dobro = numero * 2

print(f"O dobro de {numero} é {dobro}")

#Missão 10: Contando Letras 🔄

nome=input("Digite seu nome: ")
print (len(nome))