lista = ['gomes', 'cicrano', 'fulano', 'beltrano', 'maria', 'pedro']

print(lista)

#imprimindo valor especifico da lista
print(lista[0])

#imprimindo ultimo indice 
print(lista[-1])

#imprimir intervalo
print(lista[2:4])

#ordenar essa lista
#lista.sort()

#adicionando na lista
lista.append('barbosa')

#inserindo em posição especifica 
lista.insert(2, 'joao')

#inserindo varios valores
lista.extend(['ana', 'beatriz', 'david', 'roberto'])

numeros = []

#adcionando valores  de forma dinamica 
for i in range(10):
    numeros.append(i * 2)
print(numeros)    


#for i in range(len(lista)):
 #   print(f'{i+1}º valor da lista: {lista[i]}')


 #removendo itens da lista
print(f'lista antes de remover  {lista}')

# pop - remove pelo indice 
lista.pop(0)

# removendo o ultimo indice
lista.pop()

# removendo pelo valor, (remove a primeira ocorrencia)
lista.remove('cicrano')

lista_numeros = [ n for n in range(1,11)]
#removendo intervalo de valores 
del lista[2:4]


print(f'lista antes de remover  {lista}')
