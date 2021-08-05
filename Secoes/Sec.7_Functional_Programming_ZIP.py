#function: map, filter, zip, and reduce

#2) ZIP function
# cria uma tupla pareando os dados deuma variável e com os dados de outra  variável (desde que iterável)
# exemplo: posso criar lista ou dicionários com os itens de variáveis diferentes

minha_lista=['a','b','f','n']
sua_lista=[7,8,9,10]
print(dict(zip(minha_lista,sua_lista)))
#   resultado
#{'a': 7, 'b': 8, 'f': 9, 'n': 10} => o resultado só retorna os itens que podem ser pareados.

# Caso uma das variáveis possua um item a mais do que a outra, o item excedente não participará do resultado final
#exemplo
minha_lista1=['a','b','f','n','z']
sua_lista1=[7,8,9,10]
print(dict(zip(minha_lista1,sua_lista1)))
#resultado
#{'a': 7, 'b': 8, 'f': 9, 'n': 10} => veja que o item 'z' da lista 'minha_lista1' não aparece no resultado final,
# já que não foi pareado.

#ou

minha_lista2=(1,4,6,8)
sua_lista2=[17,654,34]
print(list(zip(minha_lista2,sua_lista2)))

#   resultado
#[(1, 17), (4, 654), (6, 34)] => veja que o item '8' de minha_lista2 não aparece no resultado da lista de 'zip' que fiz
#dado que ele não possui par para iterar. Quando uso a função lista em um zip, o resultado itera via tuplas ().