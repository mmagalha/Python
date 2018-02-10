#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = str(input("Digite seu nome completo: "))
print("Analisando seu nome ...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))
s = nome.split()
print("Seu primeiro nome é {} e tem {} letras".format(s[0], len(s[0])))
