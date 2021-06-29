class PlayerCharacter:
    membership=True #Class object Attributo - Atributo de classe. É um atributo que é estático em toda a classe. Não podemos mudar o valor dele se usarmos os métodos desta classe. Não é dinâmico com os atributos dos métodos

    def __init__(self, name='Anonimo', age=0): #método
     if (age >18):
       self.name=name #atributos: propriedades que os objetos possuem.Podemos acessar esses atributos colocando .e o nome do atributo
       self.age=age
     else:
        print(f'Sorry, {name}, but you are underaged')

    def shout(self): #a definição de uma função é um método, que define uma ação.
         print(f'My name is {self.name}') #quando quero chamar o método 'run', preciso colocar os (), uma vez que os métodos exigem uma ação.

player1=PlayerCharacter('Igor',31)
player2=PlayerCharacter('Gabriel',0.7)
print(player1.shout())#não colocamos () depois dos atributos pois não queremos que eles façam uma ação. ações são ligadas a métodos
print(player2.membership)