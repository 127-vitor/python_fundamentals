# while True:

#     try:
#         x = int(input('Digite o primeiro número: '))
#         y = int(input('Digite o segundo número: '))
#         print(x + y)
#         break
#     except ValueError as e:
#         print(e.with_traceback)
#         continue
#     except TypeError as v:
#         print(v.with_traceback)
#         continue
#     finally:
#         print('calculando...')

# try:
#     produto_id = [1111, 1112, 1113, 1114, 1115]
#     id_desejado = int(input('Digite o ID do produto: '))
#     if id_desejado not in produto_id:
#         raise ValueError('Produto não cadastrado!')
#     else:
#         print('Produto cadastrado!')
# except ValueError as e:
#     print(e)


