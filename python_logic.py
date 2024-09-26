# Comments are made with #
a = "45"
A = 12
a_A = 45

# variables are case sensitive. Variables can't use - only _

# Python use snake_case to variables and functions and CapitalCamelCase to classes

# Base data structures are lists, ducts, sets and tupples

tupla = (1, 2)  # Immutable 
lista = [1, 2]  # Muttable 
dicionário = {"A": 1, "B": 2}  # Key-Value pairs 
conjunto = {1, 2}  # Unique values


# Loops and conditionals
# In python we don't have blocks delimiters. We delimit blocks using indents.

for i in range(10):
    print(i)


if 5 < 10:
    print("Menor")

# Tô declare a function, use the word def

def func():
    print("Hello")


func()  # This is how we call a function.


##############################
### Simple Examples ###

# A function to determine the average of two numbers
def média(a, b):
   return (a + b) / 2

média(5, 12)


# A function to determine if someone is able to vote in Brazil


def pode_votar(idade: int) -> tuple[bool, str]:
    if idade >= 16 and idade < 18:
        return True, "Pode votar"
    elif idade >= 18 and idade < 60:
        return True, "Tem que votar"
    elif idade >= 60:
        return True, "Pode votar
    else:
        return False, "Não pode votar"


vota, status = pode_votar(50)
print(vota)
print(status)


# A function to determine if one of the pairs can vote

def random_function_without_purpose():
    pares = [{"nomes": ("Carlos", "Roberto"), "idades": (15, 32)}, {"nomes": ("Maria", "Simão"), "idades": (25, 8)}, {"nomes": ("Adalberto", "Josicreia"), "idades": (57, 78)}]

    for par in pares:
        idade_média = média(par["idades"])
        idade_média_vota = pode_votar(idade_média)
        print(f"Alguém com a idade média entre {par["nomes"][0]} e {par["nomes"][1]} {idade_média_vota[1]}")



    
# For the last. Objects are the base of OOP, one if the paradigms of Python, and one of the most important ones.
# Other paradigm of Python is it being functional, and you will see this while we work on the project.
# OOP (Object Oriented Programming) consists of using Classes and Objects primarily.
# A class is like a blueprint of an object

# Simple Class

class Caneta:
    cor: str
    tampada: bool = True
    carga: float = 1

    def __init__(self, cor: str):
        self.cor = cor

    def tampar():
        self.tampada = True

    def destampar():
        self.tampada = False

    def escrever():
        if self.tampada or self.carga == 0:
            return "Não foi possível escrever"
        self.carga -= 0.1
        return "Escrevi com sucesso"



minha_caneta = Caneta("azul")
outra_caneta = Caneta("preta")
outra_caneta.destampar()
print(minha_caneta.escrever())
minha_caneta.destampar()
outra_caneta.tampar()
print(minha_caneta.escrever())







