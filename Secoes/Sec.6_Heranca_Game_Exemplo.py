#Users
    #login
#classes: Wizard, Archer, Ogres
    #cada classe possui nome e força

class User (): #Classe pai. Todas as subclases que derivam dela, só poderão rodadas caso a premissa definida na classe pai seja realizada. Neste caso, só podemos criar os objetos wizard e archer se o usuário logar
    def __init__(self,email):
        self.email=email

    def sign_in(self): #não usamos o def __init__ pois não estamos criando métodos com parâmetros. Estamos apenas escrevendo uma frase na tela. O def __init__ é necessário para funções que contenham parâmetros e ações, por exemplo
        print('Logged in')

class Wizard(User): #Herança: colocamos o User da classe User nesta subclasse (ou classe filha) para que este objeto só possa ser criado se o login ocorrer (previsto na classe User).
    def __init__(self, name, power,email):
        super().__init__(email)     #super()= Puxa da classe pai o parâmetro desejado.Assim, não precisamos criar o parâmetro 'email' e self.email em todas as subclasses.
        self.name=name
        self.power=power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User): #Herança: Classe filha de User
    def __init__(self, name, numb_arrows,email):
        super().__init__(email)
        self.name=name
        self.numb_arrows=numb_arrows
    def check_arrow(self):
        print(f'{self.numb_arrows} left')

class Hib(Wizard,Archer):

wizard1=Wizard('Igor',23,'igor.dr@gmail.com')
archer1= Archer('Thomas',89,'thom@gmail.com')
hb=Hib('FSAD',54,43,'t4terer')
print(hb.power)