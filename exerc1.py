#Escreva um programa que leia o nome de um funcionário, seu número de horas trabalhadas
#o valor que recebe por hora e calcula o salário desse funcionário. 
#A seguir, mostre o nome e o salário do funcionário.

nome_funcionario = input('Digite o nome do colaborador: ')
horas = float(input('Digite o número de horas que este colaborador trabalha: '))
valor_hora = float(input('Digite o valor que este colaborador recebe por hora: '))

salario = horas * valor_hora

print('O colaborador', nome_funcionario, 'recebe o salário de R$', salario)
