import math

print('Função de segundo grau')

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))

delta = (B ** 2) - (4 * A * C)
raiz_delta = math.sqrt(delta)
bhaskara1 = (-B + raiz_delta) / (2 * A)
bhaskara2 = (-B - raiz_delta) / (2 * A)

print('Resultado X:', bhaskara1)
print('Resultado Y:', bhaskara2)