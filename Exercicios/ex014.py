#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celcius = float(input('Digite a temperatura em °C: '))
print('{}°C equivalem a {}°F'.format(celcius, (1.8*celcius)+32))
print('{}°C equivalem a {}°K'.format(celcius, (celcius+273.15)))
