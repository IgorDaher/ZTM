#list, set, dictionary comprehensions

# SET and DICTIONARY COMPREHENSIONS

# A MESMA COISA QUE O LIST COMPREHENSIONS MAS SUBSTITUINDO O [] POR {}.
# LEMBRANDO QUE SET É UM CONJUNTO DE ITERÁVEIS NÃO DUPLICADOS (retorna um conjunto sem itens duplicados)

my_set={char for char in 'cotonete'}
my_set2={num for num in range(0,16)}
my_set3={num**2 for num in range(0,16)}
my_set4={num**2 for num in range(0,16) if num % 2==0}

print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)

#DICTIONARY COMPREHENSIONS

# Para fazer um dict comprehensions, preciso criar um dicionário como base de dados (variável com um dicionário)
# para poder fazer o comprehension fazendo uma ação em cima da chave ou valor (primeiros parâmetros antes do for loop)
simple_dict={'a':3, 'b':4} #criado o dicionário base
my_dict={key:value**2 for key,value in simple_dict.items()} #elevei os valores à segunda potencia (value**2) e
                                                            #utilizei o simple_dict com o método ".items()" para
                                                            #listar em tuplas os dois novos valores que serão criados
                                                            #dentro do my_dict
                                                            #The method items() returns a list of
                                                            #dict's (key, value) tuple pairs

print(my_dict)

my_dict_pares={key:value**2 for key,value in simple_dict.items() if value %2==0}
print(my_dict_pares)

#caso queira fazer um dict. comprehension em uma lista,
# de maneira que a key seja o item da lista e o valor seja o próprio item dobrado, podemos fazer da seguinte forma:

dict_2={num:num*2 for num in range(0,4)} #posso substituir o range() por [0,1,2,3]
print(dict_2)
#retorno:{0: 0, 1: 2, 2: 4, 3: 6}