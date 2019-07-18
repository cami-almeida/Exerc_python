import math

print('Função de segundo grau')

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))

delta = (B ** 2) - (4 * A * C)
delta = math.sqrt(delta)
bhaskara1 = (-B + delta) / (2 * A)
bhaskara2 = (-B - delta) / (2 * A)

print('Resultado X1:', bhaskara1)
print('Resultado X2:', bhaskara2)