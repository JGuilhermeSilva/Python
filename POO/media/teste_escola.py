from escola import Disciplina

mat = Disciplina('Matematica', [7.0, 8.5])

print(f"Disciplina: {mat.nome}")
print(f"Média: {mat.calcularMedia():.2f}", end=' ||| ')
print(f"Situacao: {mat.exibirSituacao()}")
#mat.exibirSituacao()