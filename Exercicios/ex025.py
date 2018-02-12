#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Digite seu nome completo: ")).lower()
#print((nome.find('silva') >= 0))
print('Seu nome tem Silva ? {}'.format('silva' in nome))