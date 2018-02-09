#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
val = input('Digite algo: ')
print('O tipo primitivo é ? {}'.format(type(val)))
print('É alfanumérico ? {}'.format(val.isalnum()))
print('É alfa ? {}'.format(val.isalpha()))
print('É decimal ? {}'.format(val.isdecimal()))
print('É um dígito ? {}'.format(val.isdigit()))
