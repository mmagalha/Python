#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário atual R$: '))
reajuste = float(input('Digite o valor do rejuste %: '))
print('O valor do salário atual é de R${}, com reajuste de {}% o novo salário será de R${}'.format(salario, reajuste, salario+(salario*(reajuste/100))))