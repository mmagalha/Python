#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite o valor em Metros: '))
print('{:.2f} m equivale a: \n{:.0f} cm\n{:.0f} mm'.format(m, m*100, m*1000))
