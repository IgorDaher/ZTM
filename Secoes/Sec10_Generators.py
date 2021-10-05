#Aula - Generator

#Generator é uma função iterável, ou seja, aceita que os itens incluídos nela entrem em loop (função for, por exemplo).
#O objetivo de um generator é não gravar um local na memória com uma lista, por exemplo, o que faz economizar espaço.
#Exemplo. Para gerarmos o output "1,2,3,4,5,6,7,8,9,10", fazemos o seguinte:

#   def make_list(num): #criamos uma função de gerar lista sequencial (números sucessivos), por exemplo.
#       result=[] #colocamos como resultado uma lista vazia
#           for i in range (num):#criamos a função for para criar o loop com os números desejados
#               result.append(i+1) #de cada resultado da função for nós somamos 1 ao item e iteramos ele à lista vazia (append)
#           return  result #geramos o resultado final da lista iterada

#   lista_ate_dez=make_list(10) #lista que quero como output
#   print(lista)

#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Desta forma, criamos uma lista própria

# Ao invés de fazermos a função "make_list" e gastarmos espaço na memória com a variável lista_ate_dez, podemos demonstrar
# o output desejado (numeros de 1 a 10) sem ocupar espaço na memória com a variável.
# #Isso se dá com o uso de uma função de geração, a generator_func, ou simplesemente Generator.
#Vejamos o mesmo exemplo. Quero um output de 1 a 10

def generator_func(num):
   for i in range(num): #estabelecemos uma range com um limite qualquer
        yield i+i #usamos 'yield' ao invés de 'result' para pausar a função
                  # e demonstrar o output sem gastar espaço da memória

for i in generator_func(100):
    print(i)


