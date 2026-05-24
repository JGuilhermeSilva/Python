class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    def apresentar(self):
        print (f"Nome: {self.nome} / Idade: {self.idade}")

    def falar(self, assunto):
        if self.comendo == False:
            if self.falando == False:
                print (f"{self.nome} está falando sobre {assunto}")
                self.falando = True
                return
            elif self.falando == True:
                print (f"{self.nome} já está falando!")
        else:
            print(f"{self.nome} não pode falar enquanto come!")

    def pararFalar(self):
        if self.falando == True:
            print(f"{self.nome} parou de falar")
            self.falando = False
        else:
            print(f"{self.nome} não estava falando")
    
    def comer(self, comida):
        if self.falando == False:
            if self.comendo == False:
                print(f"{self.nome} está comendo {comida}")
                self.comendo = True
                return
            elif self.comendo == True:
                print(f"{self.nome} já está comendo!")
                return
        else:
            print(f"{self.nome} não pode comer enquanto fala")
            
    def pararComer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não estava comendo!")
