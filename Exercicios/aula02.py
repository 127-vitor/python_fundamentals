# Dado dicionário:

# produtos = dict(produtos=dict
#                     (p1=dict(nome='Camiseta StarWars', 
#                             preço=99.90
#                             ), 
#                     p2=dict(nome='Caneca Ricky&Morty', 
#                             preço=49.90
#                            ), 
#                     p3=dict(nome='Camiseta Spidernman', 
#                             preço=69.90
#                            )
#                     )
#                 )

# try:
#     produto_desejado = input('Digite o ID do produto: ')
#     if produto_desejado not in produtos['produtos']:
#         raise ValueError('Produto inexistente!')
#     else:
#         print('Produto: {}'.format(produtos['produtos'][produto_desejado]['nome']))
#         print(f"Preço: {produtos['produtos'][produto_desejado]['preço']}")
#         nome = produtos['produtos'][produto_desejado]['nome']
#         print(f"Produto: {nome}")
#         print('Produto: '.format())      
# except ValueError as v:
#     print(f"Erro: {v}")
 
# with open('novo arquivo', 'a') as f:
#     f.write('\nMeu primeiro arquivo')
#     f.read()



# def dobra(valor):
#     return valor * 2

# print(dobra(12))

# produtos = []


# def cadastraProduto(produto):

#     return produtos.append(produto)

# def listaProdutos():
#     print(produtos)

# def deletaProduto(produto):
#     if produto in produtos:
#         produtos.remove(produto)

# cadastraProduto('Tenis')
# deletaProduto('Tenis')

# listaProdutos()

# nome = 'python'

# def linux():
#     global nome
#     nome = 'linux'
#     return nome

# linux()
# print(nome)

# def teste(var: int) -> float:
#     print(var)

# teste('casa')

# usuarios = []


# def cadastra_Pessoa(add=None):
#     pessoa = dict(nome='Renato', sobrenome='Barbosa', idade=26)
#     if add is None:
#         pass
#     else:
#         usuarios.append(pessoa)

# cadastra_Pessoa('teste')
# print(usuarios)

# frutas = []

# def insereFrutas(*args):
#     frutas.append(args)

# insereFrutas('abacaxi', 'laranja', 'limão', 'banana')
# print(frutas)

# frutas = []

# def insereFrutas(*args):
#     for f in args:
#         frutas.append(f)

# insereFrutas('abacaxi', 'laranja', 'limão', 'banana')
# print(frutas)

# camisetas = {}

# def insereCamiseta(**kwargs):
#     global camisetas
#     camisetas = kwargs
#     return camisetas

# insereCamiseta(camiseta01='StarWars', camiseta02='Vingadores')
# print(camisetas)

# dobro = lambda x: x * 2

# print(dobro(15))

# Faça uma função lambda que receba 3 valores e retorne a soma

# soma = lambda x, y, z: x + y + z

# print(soma(3,6,9))

# from functools import reduce

# números = [1, 23, 4, 45, 456, 76, 9]

# dobro = list(map(lambda x: x * 2, números))
# numeros_par = list(filter(lambda x: x % 2 == 0, números))
# soma = reduce(lambda x, y: x + y, números)

# print(dobro)
# print(numeros_par)
# print(soma)

# for i in números:
#     dobro.append(i * 2)

# n = []

# for i in números:
#     if i % 2 == 0:
#         n.append(i)

