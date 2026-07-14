'''
#leu corretamente porem desordenou alguns campos

from pypdf import PdfReader

leitor = PdfReader("Teste_Despesas.pdf")

# Percorre todas as páginas e extrai o texto visível
for i, pagina in enumerate(leitor.pages):
    texto = pagina.extract_text()
    print(f"--- Conteúdo da Página {i + 1} ---")
    print(texto)'''


#com pdfplumber
import pdfplumber

caminho_pdf = "Teste_Despesas_Oficial.pdf"

with pdfplumber.open(caminho_pdf) as pdf:
    for i, pagina in enumerate(pdf.pages):
        print(f"--- Página {i + 1} ---")
        
        # O parâmetro layout=True força a biblioteca a respeitar a posição visual do texto
        texto = pagina.extract_text(layout=True)
        print(texto)