# Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
# quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
# uma mensagem explicativa, conforme exemplo.

nome = input('Digite o nome do funcionário: ')
valor = float(input('Digite o valor que ele recebe por hora: '))
horas = int(input('Informe a quantidade de horas trabalhadas: '))
pagamento = valor * horas
print(f'O pagamento para {nome} deve ser R$ {pagamento:.2f}')