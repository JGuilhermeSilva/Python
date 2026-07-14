#programa que calcula a media de 3 notas do aluno

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3

def resultado(media):
    if media>=7:
        return "Aprovado"
    else:
        return "Reprovado"