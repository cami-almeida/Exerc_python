import math

print('Função de segundo grau')

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

delta = (B ** 2) - (4 * A * C)

if delta>=0:
    raiz_delta = math.sqrt(delta)
    x1 = (-B + raiz_delta) / (2 * A)
    x2 = (-B - raiz_delta) / (2 * A)
    print('Resultado X1:', x1)
    print('Resultado X2:', x2)
else:
    print('Delta negativo. Não foi possível')