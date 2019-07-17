valor = None
par = []
impar = []
lista = []
while len(lista) < 10:
    valor = int(input('Digite o valor para inserir na lista: '))
    if valor % 2 == 0:
        par.append(valor)
        lista.append(valor)
    else:
        impar.append(valor)
        lista.append(valor)

print('Pares:', par)
print('Impares:', impar)