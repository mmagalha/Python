#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um número: '))
print('A parte inteira do número {} é {}'.format(num, math.trunc(num)))