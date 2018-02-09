#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Digite o valor em R$: '))
print('Com R${} você compra U${}'.format(real, (real/3.20)))