"""
Um iterator é um elemento que possui a função iter e next, uma string pode ser iterada pois por baixo dos panos o python cria um iterador para a string

nome = 'Geek'

it1 = iter(nome)

print(next(it1))
print(next(it1))

--------------------------- Criando iterador

class Contador:

    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in Contador(1, 61):
    print(n)

--------------------------- Criando uma função geradora

A função geradora é como um iterator, o yield é onde a função vai parar e esperar a próxima instrução next, quando acabar as instruções, no caso abaixo, quando acabar o while,
o next vai retornar o erro StopIteration que é quando o iterável chega ao fim assim como as strings ou listas.

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(70)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

--------------------------- Teste de memória e velocidade para comparar listas e geradores
"""

import time

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

################################### Memória: 6.2MB - 10.4MB = 4.2MB
################################### Tempo: 334.84976506233215 
# start_time_gen = time.time()
# for n in fib_gen(100000):
#     print(n)
# end_time_gen = time.time()

################################### Memória: 6.1MB - 475.7MB = 469.6MB
################################### Tempo: 350.16357135772705
# start_time_lista = time.time()
# for n in fib_lista(100000):
#     print(n)
# end_time_lista = time.time()

# print(f"Tempo lista: {end_time_lista - start_time_lista}")
# print(f"Tempo generator: {end_time_gen - start_time_gen}")