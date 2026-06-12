'''#importar as bibliotecas necessarias
import tkinter as tk #biblioteca grafica
from tkinter import messagebox #importa caixas de mensagem
from abc import ABC, abstractmethod #para criar classes abstratas

#classe abstrata  que define o contrato para qualquer transporte escolar
class TransporteEscolar(ABC):
    def __init__(self, motorista, capacidade):
        self.motorista = motorista
        self.capacidade = capacidade

    @abstractmethod
    def transportar(self): #cada transporte deve implementar como levará os estudantes
        pass

#classe onibus herda de Transporte
class Onibus(TransporteEscolar):
    def __init__(self, motorista, capacidade):
        super().__init__(motorista, capacidade)
        self.__alunos = []

    def adicionarAluno(self, nome):
        #adiciona aluno ao onibus se houver vaga
        if len(self.__alunos) < self.capacidade:
            self.__alunos.append(nome)
            return f"Aluno: {nome} entrou no ônibus"
        else:
            return "Ônibus lotado! Não ha vagas"
        
    def transportar(self):
        return f"Ônibus conduzido por {self.motorista} está levando {len(self.__alunos)} alunos"

#classe VAN herda de TransporteEscolar    
class Van(TransporteEscolar):
    def transportar(self):
        return f"Van conduzida por {self.motorista} está levando até {self.capacidade} alunos"

#classe Carro 
class Carro(TransporteEscolar):
    def transportar(self):
        return f"Carro conduzido por {self.motorista} está levando ate {self.capacidade} alunos"
    
#criando a interface grafica
class SistemaTransporte:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de transporte Escolar")

        self.veiculos = {}

        #campo de entrada para motorista, capacidade e aluno
        tk.Label(root, text="Motorista:").grid(row=0, column=0)
        self.motorista_entry = tk.Entry(root)
        self.motorista_entry.grid(row=0, column=1)

        tk.Label(root, text="Capacidade:").grid(row=1, column=0)
        self.capacidade_entry = tk.Entry(root)
        self.capacidade_entry.grid(row=1, column=1)

        tk.Label(root, text="Aluno").grid(row=2, column=0)
        self.aluno_entry = tk.Entry(root)
        self.aluno_entry.grid(row=2, column=1)

        #botoes para cadastrar os veiculos e adicionar alunos
        tk.Button(root, text="Cadastrar Onibus", command=self.cadastrar_onibus).grid(row=3, column=0, columnspan=2)

        tk.Button(root, text="Cadastrar Van", command=self.cadastrar_van).grid(row=4, column=0, columnspan=2)
        
        tk.Button(root, text="Cadastrar Carro", command=self.cadastrar_carro).grid(row=5, column=0, columnspan=2)

        tk.Button(root, text="Adicionar Aluno ao onibus", command=self.adicionar_aluno_onibus).grid(row=6, column=0, columnspan=2)

        tk.Button(root, text="Relatorio transporte", command=self.relatorio).grid(row=7, column=0, columnspan=2)

    #funcao para cadastrar onibus
    def cadastrar_onibus(self):
        motorista = self.motorista_entry.get()
        capacidade = int(self.capacidade_entry.get())
        self.veiculos["onibus"] = Onibus(motorista, capacidade)
        messagebox.showinfo("Cadastro", f"Ônibus cadastrados com motorista {motorista} e a capacidade {capacidade}.")

    def cadastrar_van(self):
        motorista = self.motorista_entry.get()
        capacidade = int(self.capacidade_entry.get())
        self.veiculos["van"] = Van(motorista, capacidade)
        messagebox.showinfo("Cadastro", f"Van cadastrada com motorista {motorista} e a capacidade {capacidade}.")

    def cadastrar_carro(self):
        motorista = self.motorista_entry.get()
        capacidade = int(self.capacidade_entry.get())
        self.veiculos["carro"] = Carro(motorista, capacidade)
        messagebox.showinfo("Cadastro", f"Caro cadastrado com motorista {motorista} e a capacidade {capacidade}.")

    def adicionar_aluno_onibus(self):
        if "onibus" in self.veiculos:
            aluno = self.aluno_entry.get()
            msg = self.veiculos["onibus"].adicionarAluno(aluno)
            messagebox.showinfo("Aluno", msg)
        else:
            messagebox.showerror("Erro", "Nenhum onibus cadastrado")
    def relatorio(self):
        if self.veiculos:
            relatorio = ""
            for v in self.veiculos.values():
                relatorio += v.transportar() + "\n"
            messagebox.showinfo("Relatório", relatorio)
        else:
            messagebox.showerror("Erro", "Nenhum veiculo cadastrado")     

#executando o sitema
root = tk.Tk()
app =SistemaTransporte(root)
root.mainloop()
'''

#importar as bibliotecas necessarias
import customtkinter #biblioteca grafica
from tkinter import messagebox #importa caixas de mensagem
from abc import ABC, abstractmethod #para criar classes abstratas

#classe abstrata  que define o contrato para qualquer transporte escolar
class TransporteEscolar(ABC):
    def __init__(self, motorista, capacidade):
        self.motorista = motorista
        self.capacidade = capacidade

    @abstractmethod
    def transportar(self): #cada transporte deve implementar como levará os estudantes
        pass

#classe onibus herda de Transporte
class Onibus(TransporteEscolar):
    def __init__(self, motorista, capacidade):
        super().__init__(motorista, capacidade)
        self.__alunos = []

    def adicionarAluno(self, nome):
        #adiciona aluno ao onibus se houver vaga
        if len(self.__alunos) < self.capacidade:
            self.__alunos.append(nome)
            return f"Aluno: {nome} entrou no ônibus"
        else:
            return "Ônibus lotado! Não ha vagas"
        
    def transportar(self):
        return f"Ônibus conduzido por {self.motorista} está levando {len(self.__alunos)} alunos"

#classe VAN herda de TransporteEscolar    
class Van(TransporteEscolar):
    def transportar(self):
        return f"Van conduzida por {self.motorista} está levando até {self.capacidade} alunos"

#classe Carro 
class Carro(TransporteEscolar):
    def transportar(self):
        return f"Carro conduzido por {self.motorista} está levando ate {self.capacidade} alunos"
    
#criando a interface grafica
class SistemaTransporte:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de transporte Escolar")

        self.veiculos = {}

        #campo de entrada para motorista, capacidade e aluno
        customtkinter.CTkLabel(root, text="Motorista:").grid(row=0, column=0)
        self.motorista_entry = customtkinter.CTkEntry(root)
        self.motorista_entry.grid(row=0, column=1)

        customtkinter.CTkLabel(root, text="Capacidade:").grid(row=1, column=0)
        self.capacidade_entry = customtkinter.CTkEntry(root)
        self.capacidade_entry.grid(row=1, column=1)

        customtkinter.CTkLabel(root, text="Aluno").grid(row=2, column=0)
        self.aluno_entry = customtkinter.CTkEntry(root)
        self.aluno_entry.grid(row=2, column=1)

        #botoes para cadastrar os veiculos e adicionar alunos
        customtkinter.CTkButton(root, text="Cadastrar Onibus", command=self.cadastrar_onibus).grid(row=3, column=0, columnspan=2)

        customtkinter.CTkButton(root, text="Cadastrar Van", command=self.cadastrar_van).grid(row=4, column=0, columnspan=2)
        
        customtkinter.CTkButton(root, text="Cadastrar Carro", command=self.cadastrar_carro).grid(row=5, column=0, columnspan=2)

        customtkinter.CTkButton(root, text="Adicionar Aluno ao onibus", command=self.adicionar_aluno_onibus).grid(row=6, column=0, columnspan=2)

        customtkinter.CTkButton(root, text="Relatorio transporte", command=self.relatorio).grid(row=7, column=0, columnspan=2)

    #funcao para cadastrar onibus
    def cadastrar_onibus(self):
        motorista = self.motorista_entry.get()
        capacidade = int(self.capacidade_entry.get())
        self.veiculos["onibus"] = Onibus(motorista, capacidade)
        messagebox.showinfo("Cadastro", f"Ônibus cadastrados com motorista {motorista} e a capacidade {capacidade}.")

    def cadastrar_van(self):
        motorista = self.motorista_entry.get()
        capacidade = int(self.capacidade_entry.get())
        self.veiculos["van"] = Van(motorista, capacidade)
        messagebox.showinfo("Cadastro", f"Van cadastrada com motorista {motorista} e a capacidade {capacidade}.")

    def cadastrar_carro(self):
        motorista = self.motorista_entry.get()
        capacidade = int(self.capacidade_entry.get())
        self.veiculos["carro"] = Carro(motorista, capacidade)
        messagebox.showinfo("Cadastro", f"Caro cadastrado com motorista {motorista} e a capacidade {capacidade}.")

    def adicionar_aluno_onibus(self):
        if "onibus" in self.veiculos:
            aluno = self.aluno_entry.get()
            msg = self.veiculos["onibus"].adicionarAluno(aluno)
            messagebox.showinfo("Aluno", msg)
        else:
            messagebox.showerror("Erro", "Nenhum onibus cadastrado")
    def relatorio(self):
        if self.veiculos:
            relatorio = ""
            for v in self.veiculos.values():
                relatorio += v.transportar() + "\n"
            messagebox.showinfo("Relatório", relatorio)
        else:
            messagebox.showerror("Erro", "Nenhum veiculo cadastrado")     

#executando o sitema
root = customtkinter.CTk()
app = SistemaTransporte(root)
root.mainloop()
