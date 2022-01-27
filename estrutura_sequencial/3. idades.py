# Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
# nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo.

print('Dados da primeira pessoa: ')
nome = input('Nome: ')
idade = int(input('Idade: '))
print()
print('Dados da segunda pessoa: ')
nome2 = input('Nome: ')
idade2 = int(input('Idade: '))
media = (idade + idade2) / 2
print()
print(f'A idade média de {nome} e {nome2} é de {media: .1f}')