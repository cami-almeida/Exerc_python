PI = 3.14
raio = float(input('Digite o valor do Raio do círculo: '))

def area():
    area = PI * (raio ** 2)
    print('Area do cículo:', area)

def comprimento():
    comprimento = 2 * PI * raio
    print('Comprimento da circuferencia', comprimento)

calc = input('Digite AREA para saber a area do círculo ou COMPRIMENTO para saber o comprimento da circuferencia: ')

if calc.lower() == 'area':
    print(area())
elif calc.lower() == 'comprimento':
    print(comprimento())
else:
    print('Cálculo não identificado.')