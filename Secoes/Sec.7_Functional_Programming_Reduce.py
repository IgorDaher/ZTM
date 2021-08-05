#function: map, filter, zip, and reduce

#4) Reduce function
# Explicação abaixo

from functools import reduce #o reduce não é uma builtin function do Python, então temos que importar da library functools

minha_lista=[1,2,3,4,5,6]

def dobrar(item): #não usada no Reduce
    return item*2

def somente_impar(item): #não usada no Reduce
    return item % 2!=0

def acumulador(ac, item):
    print(ac,item)
    return ac+item

print(reduce(acumulador,minha_lista,0)) #retorna um resultado utilizando uma
# função [acumulador], uma base de dados [minha lista] e um número inicial [0] (que poderia ser qualquer nº).
#neste caso, a função 'acumulador' retorna a soma dos itens da minha lista e,
# ao final, soma como o número inicial, que no caso é 0, retornando 21. Caso colocasse 15, seria 21+15, retornando 36.
#obs: como eu utilizei i print de (ac, item),
# a operação da função acumuladora era retornada na tela até chegar ao último item da base de dados [6].
#caso eu tire o print (ac,item) da função acumulador, será retornado apenas o resultado final de 21 (com inicial 0).