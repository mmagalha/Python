#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Digite a quantidade de dias do aluguel: '))
km = float(input('Digite a quantidade de Km rodados: '))
print('Valor total a pagar em R${}'.format((60*dias)+(km*0.15)))