class Filme:
    
    def __init__(self, id, name, year):
        self.name = name
        self.descricao = descricao
        self._id = id 

    A Hora do Hush 3 = Filme("A Hora do Hush 3", 2018, 160)
    print(A Hora do Hush 3.name)

    Jumanji = Filme("Jumanji - Bem Vindo a Selva ", 4 de janeiro de 2018)
    print(Jumanji.name)

    Annabelle - A Criação do Mal = Filme("Annabelle - A Criação do Mal", 17 de agosto de 2017)
    print(Annabelle.name)


    def get_id(self):
        return self._id 

    def set_id(self,id):
        self._id = id
        
    def get_nome(self):
        return self._nome

    def set_nome(self,nome):
        self._nome = nome
    
    def get_descricao(self):
        return self._descricao

    def set_descricao(self,descricao):
        self._descricao = descricao
