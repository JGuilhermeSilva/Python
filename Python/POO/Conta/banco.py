from classeCliente import Cliente2
from contas import Conta


cliente1 = Cliente2('Guilherme', '(83) 98652-7921', '709.653.494-62')
cliente2 = Cliente2('Teste',     '(83) 99999-9999', '123.456.789-00')
cliente3 = Cliente2('Chupetinha','(55) 4002-8922',  '000.000.000-00')
cliente4 = Cliente2('Usuario4',  '(83) 00000-0000', '111.111.111-10')

conta1 = Conta(1, 10000.00, cliente1)
conta2 = Conta(2, 10.00,    cliente2)
conta3 = Conta(3, 50.00,    cliente3)
conta4 = Conta(4, 357.00,   cliente4)

#conta1
conta1.exibirSaldo() #retorna 10000.00
conta1.depositar(50.00) #deposita 50 na conta1
conta1.exibirSaldo() #retorna 10050.00
conta1.sacar(17.00) #tira 17.00 da conta1
conta1.exibirSaldo() #retorna 10033.00

#conta2
conta2.exibirSaldo() #retorna 10.00
conta2.depositar(5) #deposita 5 na conta2
conta2.exibirSaldo() #retorna 15.00
conta2.sacar(10.00) #tira 10.00 da conta2
conta2.exibirSaldo() #retorna 5.00