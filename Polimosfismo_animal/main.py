# main.py
from mamifero import Mamifero
from passaro import Passaro
from peixe import Peixe

def main():

    # Criando os objetos das classes
    gato = Mamifero("Gato", "Doméstico")
    pardal = Passaro("Pardal", "Floresta", pode_voar=True)
    atum = Peixe("Atum", "Oceano")

    
    animais = [gato, pardal, atum]

    print("=== Detalhes dos Animais ===")
    for animal in animais:
        print(animal.detalhes())
        print(f"Som: {animal.emitir_som()}")
        # Verificando se é um Passaro para chamar o método voar
        if isinstance(animal, Passaro): 
            print(f"Ação: {animal.voar()}")
        print("-" * 30)

if __name__ == "__main__":
    main()
