import calculandoODesconto

valor = float(input("Insira o valor do produto: "))
valorFinal = calculandoODesconto.calcularDesconto(valor)

print(f"Preço original é: {valor:.2f}")
print(f"Preço com desconto de 10%: {valorFinal:.2f}")