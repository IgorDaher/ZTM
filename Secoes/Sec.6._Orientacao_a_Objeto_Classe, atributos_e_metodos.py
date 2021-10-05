class PlayerCharacter:  #Classe é o objeto que queremos criar. Para isso, definimos uma série de códigos que
    # queremos executar para quando este objeto é chamado.
    # Esta série de códigos são os métodos e atributos.
    # Eles serão utilizados para que possamos gerar o resultado desejado
    # quando chamamos o objeto e a ação que ele fará.
    def __init__(self, name, age=0): #__init__ é um dunder method (método especial). É considerado um método construtor.
        # Ele sempre é chamado quando instanciamos a classe para criar um objeto (ex: pl1 e pl2)
        #self se refere ao objeto criado que será instanciado por essa classe.
        self.name=name #atributos = propriedades de um objeto
        self.age=age #atributos

    def fala(self): #método: uma função que gera uma ação
        print(f'meu nome é {self.name} e tenho {self.age} anos')
        return "" #colocamos o 'return ""' para que a função não retorne um 'None'no output,
                  #uma vez que uma fução sem "return" gera o "None" como output


pl1=PlayerCharacter('Igor', 42) #pl1 é um Objeto. Para criar o 'pl1 e 'pl2' nós instanciamos a classe "PlayerCharacter"
                                # e definimos entre os parênteses os atributos do objeto que advém do dunder method
                                #"__init__", método especial que criamos para definir os atributos do objeto da classe
                                #"PlayerCharacter". Assim, o objeto 'pl1' terá como nome 'Igor' e como age "42".

pl2=PlayerCharacter('Gabriel',11) #Quando eu coloco o () após a classe (PlayerCharacter), ele automaticamente executa
                                # o que foi definido no dunder method (__init__)

print(pl1.name) #Quero acessar o nome do objeto pl1. Só colocar o objeto seguido de '.' e a sua propriedade
                # que quero acessar (atributo 'nome').
                #Output: 'Igor'

print(pl1.fala()) #criado o objeto e definidos os seus atributos, eu posso criar uma ação para ele com o método "fala",
                  # que criamos dentro da classe 'PlayerCharacter'.
                  # Para isso, basta colocar o objeto 'pl1' seguido de '.' e da ação (método) que criamos na classe,
                  # no caso,'fala' (pl1.fala()). Como o método é uma ação, eu devo colocar os () após escrevê-lo,
                  # para que ele possa executar o método (ação) 'fala'.
print(pl2.fala())

#Output:
#meu nome é Igor e tenho 42 anos
#meu nome é Gabriel e tenho 11 anos

