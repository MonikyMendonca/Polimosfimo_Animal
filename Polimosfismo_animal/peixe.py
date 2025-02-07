# peixe.py
from animal import Animal

class Peixe(Animal):
    def __init__(self, nome, habitat, tem_escamas=True):
        super().__init__(nome, habitat)
        self.tem_escamas = tem_escamas  

    def emitir_som(self):
        return "Som de bolhas"
