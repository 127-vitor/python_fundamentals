# Dado o dicionário:

dados = {
    'estados':{
            'sp': {
                'nome': 'São Paulo',
                'municipios': 645,
                "população": 44.04
                  },
            'rj': {
                'nome': 'Rio de Janeiro',
                'municipios': 92,
                'população': 16.72
                  },
            'mg': {
                'nome': 'Minas Gerais',
                'municipios': 31,
                'população': 20.87
                  }
              }    
}    

# print('Estado: ',dados['estados']['sp']['nome'])
# print('Municipios: ',dados['estados']['sp']['municipios'])
# print('População: ',dados['estados']['sp']['população'])

# print(f"Estado: {dados['estados']['sp']['nome']}")
# print(f"Municipios: {dados['estados']['sp']['municipios']}")
# print(f'População: {dados['estados']['sp']['população']}')

for estado in dados ['estados'].keys():
    print(f"Estado: {dados['estados'][estado]['nome']}")
    print(f"Municipios: {dados['estados'][estado]['municipios']}")
    print(f"População: {dados['estados'][estado]['população']}")
    print('')