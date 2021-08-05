#LAMBDA EXPRESSIONS
# é uma função anônima. Não ocupa espaço na memória. Ideal para se usar uma única vez.
#  lambda parametro: acão que você deseja(parâmetro)

#criando uma função de multiplicação por 2. Utilizo espaço da memória para guardá-la.

my_list=[1,2,3]

#def multiply_by2(item):
 #   return item*2

#print(list(map(multiply_by2, my_list)))

# SE EU QUISER UTILIZAR UMA FUNÇÃO DE MULTIPLICAÇÃO POR 2 UMA ÚNICA VEZ
# E NÃO PRECISAR DEFINIR UMA FUNÇÃO (EX: MULTIPLY_BY2), É SÓ UTILIZAR O MÉTODO LAMBDA:

#print(list(map(lambda item:item*2,my_list))) #no lugar de item eu poderia usar qualquer letra...

#exemplo: Elevar todos os itens da lista à segunda potência

lista=[2,4,7]

#print(list(map(lambda i:i**2,lista)))
#Retorno
#[4, 16, 49]

#uso list para trazer como retorno uma lista;
# uso map para utilizar uma 'ação e uma base de dados' específica sem precisar criar uma função com for
# e uso lambda para não precisar definir uma função de elevar à potencia (criando um def elevar_2(i):)
# e faço isso dentro da própria linha de print de retorno

#exemplo 2: ordenar a lista abaixo baseando-se no segundo item da tupla:

lis1=[(0,2),(4,3), (9,9), (10,-1)]
lis1.sort(key=lambda item:item[1])
print(lis1)