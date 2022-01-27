# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.

import math

base = float(input('Base do retangulo: '))
altura = float(input('Altura do retangulo: '))
area = base * altura
perimetro = 2 * base + 2 * altura
diagonal = math.sqrt(base ** 2 + altura ** 2)
print()
print(f'Área: {area: .4f}')
print(f'Perímetro: {perimetro: .4f}')
print(f'Diagonal: {diagonal: .4f}')

