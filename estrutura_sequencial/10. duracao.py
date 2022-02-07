# Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
# formato horas:minutos:segundos.

duracao = int(input('Digite a duração em segundos: '))

hora = duracao // 3600              #divisão inteira
resto = duracao % 3600              #resto da divisão
min = resto // 60                   #divisão inteira
seg = resto % 60                    #resto da divisão

print(f'{hora} : {min} : {seg}')

