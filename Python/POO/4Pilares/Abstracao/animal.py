from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Pato(Animal):
    def emitir_som(self):
        print("Quac Quac")

class Cachorro(Animal):
    def emitir_som(self):
        print("AU AU")

class Galinha(Animal):
    def emitir_som(self):
        print("CoCoCó")

class Bode(Animal):
    def emitir_som(self):
        print("Béééee")

animais = [Pato(), Cachorro(), Galinha(), Bode()] 
for bicho in animais:
    bicho.emitir_som()
    