#Exercicio - Criar a sequencia de Fibonacci com um Generator
#A sequencia de Fibonacci é uma sequência em que se gera uma ordem sequencial de soma entre o numero e o seu antecedente
#F0	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F13	F14	F15	F16	F17	F18	F19	F20
#0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597	2584	4181	6765

def fib(num): #criação do generator FIB, já que quero gerar o output da sequencia sem criar um espaço na memória
    a=0 #primeiro item da sequencia de fibonacci
    b=1 #segundo item da sequencia
    for i in range(num): #quero criar um generator que colocando um determinado
                        # #numero da sequencia ela me mostre a squencia de fibonacci até ele
                        #para isso, usarei o generator range com uma variável a minha escolha (num)
        yield a #quero que retorne o primeiro item da sequencia para somar ao seguinte
        temp = a #assim, a partir do retorno do primeiro item eu igualo ele a uma variável temporária
                # para que ele possa ser somado posteriormente com o numero subsequente
        a=b     #agora eu igualo o primeiro ao valor do segundo item
        b=temp+b #assim, eu somo o item temporário (igual ao primeiro numero da sequencia) com o segundo numero (b),
                # sendo o resultado a soma dos dois

for x in fib(21): #quero a sequencia de fibonacci até o item 20
    print(x)

#FAZENDO A SEQUENCIA DE FIBONACCI SEM O GENERATOR, MAS COM LISTA
    def fib2(num):
        a = 0
        b = 1
        result=[] #CRIO UMA LISTA VAZIA
        for i in range(num):
            result.append(a) #no resultado eu acrescento o 'a'
            temp=a
            a=b
            b=temp+b
        return result

    print(fib2(21))