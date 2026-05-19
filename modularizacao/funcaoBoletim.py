import boletim

nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))

media = boletim.media(nota1, nota2, nota3)
resultado = boletim.resultado(media)


print(f"Sua média foi: {media}")
print(f"Seu resultado foi: {resultado}")
