# passaro.py
from animal import Animal

class Passaro(Animal):
    def __init__(self, nome, habitat, pode_voar=True):
        super().__init__(nome, habitat)
        self.pode_voar = pode_voar 

    def emitir_som(self):
        return "Canto de ave"

    def voar(self):
        return "Estou voando!" if self.pode_voar else "Não consigo voar."
