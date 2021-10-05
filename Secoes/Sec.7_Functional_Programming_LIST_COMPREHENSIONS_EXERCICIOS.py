#EXERCICIOS LIST COMPREHENSIONS

#Encontrar os valores duplicados e colocar numa lista com o list comprehensions

#exercício resolvido com o 'for loop'.
s_list=['a','b','c','d','b','m','n','n']

duplicates=[]
for value in s_list:
    if s_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# Solução com o List Comprehensions:

duplicates2=list(set([char for char in s_list if s_list.count (char) > 1 ]))
# IMPORTANTE:
# Passo 1: usei o método .count mostra quantas vezes um item aparece numa lista
# Passo 2: Usei a built-in function SET porque a minha expressão retornaria ['b','b','n','n'].
#          com o SET, eu retiro as duplicidades do meu conjunto de dados
# Passo 3: Transformei a SET em uma LIST para poder retornar a solução do exercício como uma lista
# e ter o resultado ['n','b']
print(duplicates2)