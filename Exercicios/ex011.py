#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
print('A parede tem {}m2 e serão necessários {}l de tinta'.format((a*l), (a*l)/2))