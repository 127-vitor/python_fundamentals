from core import user_table, engine

con = engine.connect()
insert = user_table.insert()

# new = insert.values(idade=25, nome='Caio', senha='abacaxi123')
# con.execute(new)

con.execute(user_table.insert(), [{'nome':'Marcio', 'idade':20, 'senha':'limao321'},
                                {'nome':'Gustavo', 'idade':18, 'senha':'goiaba123'},
                                {'nome':'Guilherme', 'idade':22, 'senha':'maracuja456'}
                                ])