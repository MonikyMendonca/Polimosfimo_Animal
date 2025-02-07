# animal.py
class Animal:
    def __init__(self, nome, habitat):
        self.nome = nome  
        self.habitat = habitat  

    def emitir_som(self):
        raise NotImplementedError("Método 'emitir_som' deve ser implementado pela subclasse.")

    def detalhes(self):
        return f"Nome: {self.nome}, Habitat: {self.habitat}"
