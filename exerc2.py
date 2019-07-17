
valor = None
lista = []
while len(lista) < 20:
    valor = input('Digite o valor para inserir na lista: ')
    lista.append(valor)

print('O maior número é:', max(lista, key=int))