

class Pai():
    hobby = 'nadar'

    def __init__(self):
        self.profissão = 'programador'

    def mudarHobby(self):
        self.hobby = 'futebol'

jubileu = Pai()
print(id(jubileu.hobby))
jubileu.mudarHobby()
print(id(jubileu.hobby))