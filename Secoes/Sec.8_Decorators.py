#Decorators
#Tipo de função que permite ser utilizada durante todo o código,
# trazendo determinada característica a outras funções dando um

#Exemplo: Criar um Decorator para realçar algum texto no display:


def my_decorator (func):
    def wrap_func(): #wrap function é a função que é criada dentro do decorator para ser utilizada nas outras funções
        print('**********')
        func()
        print('**********')
    return wrap_func

@my_decorator #os decorators são reconhecidos por se utilziar o @ antes das funções em que serão utilizados
def hello():
    print('Igor Daher')

hello() #função hello terá seu output maximizado com a wrap_function do decorator

# Output:
# **********
#  Igor Daher
# **********

#Os decorators podem ser utilizados para criar inúmeras funções a outras funções,
#como no caso do teste de performance abaixo

from time import time #modulo de tempo/cronometro do python
def performance(fn):
    def wrapper(*args,**kwargs): #permitimos a criaçao de qualquer quantidade e tipos de parâmetros (args e kwargs)
        t1=time() #função time do módulo time
        result=fn(*args,**kwargs) #criamos a variável result para remeter a função que será utilizada pelo decorator
        t2=time()
        print(f'took {t2-t1}s') #utilizamos o print para dar o output do texto com a diferneça do tempo de processamento da função a ser utilziada
        return result
    return wrapper


@performance
def cronometro():
    for i in range(100000000):
        i*5

cronometro() #utilizamos o decorator @performance em cronometro para medir o tempo da multiplicação de todos os números na range por 5

#Exercício:
# Create an @authenticated decorator that only allows
# the function to run is user1 has 'valid' set to True:
user1 = {'name': 'Sorna','valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper (*args, **kwargs):
        if args[0]['valid']:
            return fn(*args,**kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)

