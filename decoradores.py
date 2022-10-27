############################################# Higher order functions

############################################# Funções que retornam outras funções, passar função como argumento e criar variáveis do tipo de funções

# def somar(a, b):
#     return a + b

# def diminuir(a, b):
#     return a - b

# def calcular(a, b, funcao):
#     return funcao(a, b)

# print(calcular(12, 5, somar))
# print(calcular(12, 5, diminuir))

############################################# Nested Functions

# def seja_educado(funcao):
#     def sendo_educado():
#         print("Prazer em conhecê-lo!")
#         funcao()
#         print("Tenha um bom dia!")
#     return sendo_educado

# @seja_educado
# def dormir():
#     print("Estou com sono...")

# @seja_educado
# def fome():
#     print("Estou com fome...")

# dormir()
# fome()

"""
Como usar decoradores

---------------------------------------------------------------------
|   Home    |   Servicos    |   Produtos    |   Admin   |   Login   |
---------------------------------------------------------------------

def checa_login():
    if not request.usuario:
        redirect('https://suaempresa.com.br/login')

def servicos(request):
    return 'Acesso à serviços'

def home(request):
    return 'Acesso à home'

@checa_login
def produtos(request):
    return 'Acesso à produtos'

@checa_login
def admin(request):
    return 'Acesso à administrativo'
"""