# Crie uma classe Mamifero com os atributos
#   bebe leite

# Crie uma classe homo-sapiens com os atributos:
#   Caça
#   polegares = True
#   formaCaminhar = 'Bípede'
# Métodos:
#   Caçar
#   Comer
#   Dormir
#   Construir

class Mamifero():

    def __init__(self):
        self.bebeleite = 'Sim'

class Homo_sapiens(Mamifero):

    def __init__(self):
        Mamifero.__init__(self)
        # super().__init__()
        self.caça = True
        self.polegares = True
        self.formaCaminhar = 'Bípede'

    def Caçar(self):
        print('Caçando...')

    def Comer(self):
        print('Comendo...')

    def Dormir(self):
        print('Dormindo...')

    def Construir(self):
        print('Construindo...')

c001 = Homo_sapiens()
print(c001.bebeleite)
print(c001.caça)
print(c001.polegares)
print(c001.formaCaminhar)
c001.Caçar()
c001.Comer()
c001.Dormir()
c001.Construir()