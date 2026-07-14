class Disciplina:
    def __init__(self, nome, notas):
        self.nome = nome,
        self.notas = notas

    def calcularMedia(self):
        return (self.notas[0] + self.notas[1])/2

    def exibirSituacao(self):
        media = self.calcularMedia()
        
        if media>=6.0:
            return ("aprovado")
        elif media>=3:
            return ("recuperacao")
        else:
            return ("Reprovado")
