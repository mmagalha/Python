#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o valor do angulo: '))
print('O o Sen, Cos e Tg do angulo {} valem respectivamente {}, {} e {}'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))