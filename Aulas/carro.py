# -*- coding: UTF-8 -*-

#classe

# class Automovel():
#     def __init__(self):
#         self.motor = 'Combustão'

# class Carro():
    
    #métodos da classe
#     def __init__(self):
#         Automovel.__init__(self)
#         self.rodas = 4
#         self.porta_mala = 'Normal'
#         self.motor = True
#         self.volante = True
#         self.tanque = True
    
#     def ligar(self):
#         print('carro ligado')
    
#     def desligar(self):
#         print('carro desligado')
    
#     def acelerar(self):
#         print('acelerando')
    
#     def frear(self):
#         print('freando')

# #objeto
# objetoCarro= Carro()

# objetoCarro.ligar()
# objetoCarro.acelerar()

# class Fiat147(Carro):

#     def __init__(self):
#         super().__init__()
#         Carro.__init__(self)
#         self.motor = 'Elétrico'
#         self.porta_mala = 'Com agua'


# c001 = Fiat147()
# print(c001.motor)

class Pai():
    hobby = 'Programar'
    def __init__(self):
        self.profissão = 'Advogado'

    def mudarProfissão (self, nova_profissão):
        self.profissão = nova_profissão

    def mudarHobby(self):
        self.hobby = 'Jardineiro'

joão = Pai()

joão.mudarProfissão('Carpinteiro')
joão.mudarHobby()
print(joão.hobby)





class Mãe():

    hobby = 'vender miçanga'

    def __init__(self):
        self.profissão = 'Médica'

class Filho(Pai, Mãe):

    def __init__(self):
        Pai.__init__(self)
        self.profissão = 'Programador'

jose = Filho()

print(jose.profissão)


