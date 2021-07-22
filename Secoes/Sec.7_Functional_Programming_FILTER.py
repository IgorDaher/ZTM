#function: map, filter, zip, and reduce

#2) FILTER function
# retorna, de acordo com um resultado booleano (True or False), uma ação determinada por uma função para uma determinada base de dados (que pode ser uma variável)


minha_lista=[1,2,3,4,5,6]
def dobrar(item):
    return item*2

def somente_impar(item):
    return item % 2!=0

lista_impar=(list(filter(somente_impar,minha_lista)))
print(minha_lista)
print(lista_impar)

#ou, caso não queira criar uma variavel chamada lista impar,
# mas queira apenas retornar os números impares de 'minha_lista', basta dar 'print(list(filter(somente_impar, minha_lista)))

