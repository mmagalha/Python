#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = int(input('Digite e primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
print('A média entre as notas {} e {} vale {}'.format(n1, n2, (n1+n2)/2))
