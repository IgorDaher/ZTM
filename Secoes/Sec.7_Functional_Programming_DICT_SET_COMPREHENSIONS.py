#list, set, dictionary comprehensions

# LIST COMPREHENSIONS

#Como usualmente se cria uma lista com as letras de uma palavra, por exemplo:

my_list=[] #variável com uma lista vazia para eu colocar as letras

for letra in 'igor': #crio um 'for' loop para ele ir acrescentando as letras dentro da lista
    my_list.append(letra) #usar o método append para colocar os itens na variável

print(my_list)
#retorno:
# ['i', 'g', 'o', 'r']

#CONTUDO, EXISTE UM MEIO MAIS LIMPO DE SE REALIZAR ESSA OPERAÇÃO, QUE É COM - NESTE CASO - O LIST COMPREHENSIONS
#(PODERIA SER SET OU DICTIONARY)
#COMO É UTILIZADO LIST COMPREHENSION?

#my_list=[parametro for parametro in variavel_iterável]. Utilizo o for loop dentro da própria lista,
                                                        # tornando o código mais enxuto. Exemplo:

sy_list=[letra for letra in 'gabriel'] # utilizo o 'for' para realizar uma açao em loop
                                        #(separar as letras da string gabriel) em (in) uma variável iterável,
                                        # no caso, uma string ('gabriel')
print(sy_list)
#retorno:
#['g', 'a', 'b', 'r', 'i', 'e', 'l']

#Posso usar a mesma lógica para criar uma lista com um range de números (de 0 a 15, por exemplo):

ny_list=[num for num in range(0,16)]
print(ny_list)

# IMPORTANTE!!!! E se eu quisesse criar uma lista de 0 a 15 com estes números multiplicados elevados à segunda potência?

# A RESPOSTA É SIMPLES: O PRIMEIRO 'NUM' (ANTES DO 'FOR' LOOP) É UMA EXPRESSÃO
# UTILIZADA PARA MOSTRARMOS COMO QUEREMOS AGIR SOBRE AQUELE PARÂMETRO.
# DESTA FORMA, DEVEMOS APOR A AÇÃO NESTE PRIMEIRO PARAMETR0 [num**2 for num in range(0,16]

ny_list2=[num**2 for num in range (0,16)]
print(ny_list2)

# Mas e se eu quisesse que da lista ny_list2 só aparecessem os números pares, como faríamos?
# UTILIZA-SE UMA EXPRESSÃO DE CONDICIONAL 'IF' AO FINAL DA EXPRESSÃO
# OBRIGANDO QUE À LISTA SÓ FOSSEM INSERIDOS OS PARES (num % 2==0)
ny_listpares=[num**2 for num in range (0,16) if num % 2 ==0]
print(ny_listpares)