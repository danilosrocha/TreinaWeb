class NoArvore():
    def __init__(self, valor, no_esq = None, no_dir = None):
        self.__valor = valor
        self.__no_esq = no_esq
        self.__no_dir = no_dir

    @property
    def valor(self):
        return self.__valor

    @property
    def no_esq(self):
        return self.__no_esq

    @property
    def no_dir(self):
        return self.__no_dir

    @no_esq.setter
    def no_esq(self, no_esq):
        self.__no_esq = no_esq
    
    @no_dir.setter
    def no_dir(self, no_dir):
        self.__no_dir = no_dir
