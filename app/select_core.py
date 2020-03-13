from sqlalchemy import select
from core import user_table


# Select
selecione = select([user_table])
# print([x for x in selecione.execute()])

# Select com filtro
filtro = input('Digite o nome do usuario: ')

selecione_filtro = select([user_table]).where(user_table.c.nome == filtro)

print([f for f in selecione_filtro.execute()])

# lista = [i*2 for i in range(10)]

# ou

# for i in range(10):
#     lista.append(i * 2)
    
# print(lista)