class Noticia:

    def __init__(self, id, nome, data, titulo, img):
        self.__id = id
        self.__nome = nome
        self.__data = data
        self.__titulo = titulo
        self.__img = img    
        
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome 

    def get_data(self):
        return self.__data

    def get_titulo(self):
        return self.__titulo

    def get_img(self):
        return self.__img

class Estado:
    def __init__(self, id, nome, sigla, bandeira):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__bandeira = bandeira
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_sigla(self):
        return self.__sigla
    
    def get_bandeira(self):
        return self.__bandeira