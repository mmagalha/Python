#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
nome = str(input('Digite a frase: ').lower())
print('A letra A aparece {} vezes na frase {}'.format(nome.count('a'), nome))
print(nome.find('a'))
print(nome.rfind('a'))
