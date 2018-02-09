#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o valor do produto: '))
print('O produto tem preço original de R${:.2f}, com desconto o valor é de R${:.2f}'.format(preco, (preco * 0.95)))