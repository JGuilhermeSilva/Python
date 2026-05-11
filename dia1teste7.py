idade = int(input("Insira sua idade: "))
cnh = str(input("Tem CNH? sim ou nao? "))
if (idade >= 18 and cnh=="sim"):
    print("pode dirigir")
else:
    print("Nao pode dirigir") 
    #print('nao sei')