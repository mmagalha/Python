#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input("Digite um número entre 0 e 9999: "))
print("Analisando o número {} temos: ".format(n))
print("Unidade: {}".format(n // 1 % 10))
print("Dezena:  {}".format(n // 10 % 10))
print("Centena: {}".format(n // 100 % 10))
print("Milhar:  {}".format(n // 1000 % 10))