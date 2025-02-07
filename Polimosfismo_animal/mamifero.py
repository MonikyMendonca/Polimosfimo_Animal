# mamifero.py
from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, habitat, tem_pelos=True):
        super().__init__(nome, habitat)
        self.tem_pelos = tem_pelos 

    def emitir_som(self):
        return "Som de mamífero"
