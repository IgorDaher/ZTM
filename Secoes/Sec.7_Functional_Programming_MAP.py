#function: map, filter, zip, and reduce

#1) MAP function
# map(ação, dados)
#ex: map(dobrar, [1,2,3])
# ao invés de usar a função abaixo
#def dobrar(lista):
#    new_list=[]    #eu substituto todas essas linhas (<-)
#    for i in lista: (<-)
#      new_list.append(i*2) (<-)
#    return (new_list) (<-)
#
# por
# def dobrar(lista):
#    return lista*2

# print(list(map(dobrar,[1,2,3,5]) => uso o 'list' para converter os dados (que viraram um objeto [object] na memória) para uma lista.
# se usar apenas o print(map(dobrar,[1,2,3,5]) o retorno será o local do objeto na memória (map object at 0x0578B0)
# a função map permite aplicar qualquer função pura a uma variável iterável

#        Retorno
#[2, 4, 6, 10]

# se eu criar uma variável
#minha_lista=[1,3,5,7]
#def dobrar(lista):
 #   return lista*2

#print(list(map(dobrar,minha_lista)))
#print(minha_lista)

#       Retorno
#[2, 6, 10, 14]
#[1, 3, 5, 7]  #a variável minha_lista permanece intacta


minha_lista=[1,3,5,7]
def dobrar(lista):
    return lista*2

print(list(map(dobrar,minha_lista)))
print(minha_lista)















