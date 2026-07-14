use ponto_eletronico;

-- criar tabela de funcionarios
create table Funcionarios(
	id int auto_increment primary key,
    nome varchar(50),
    cargo varchar(30),
    departamento varchar(30)    
);

-- cria tabela de registros de ponto
create table RegistrosPonto(
	id int auto_increment primary key,
    funcionario_id int,
    data Date,
    hora_entrada Time,
    hora_saida Time,
    foreign key (funcionario_id) references Funcionarios(id)
);


-- inserindo fuincionarios ficticios
insert into Funcionarios(nome, cargo, departamento) values
('Guilherme', 'Programador', 'Desenvolvimento de Sistemas'),
('Lindomara', 'Esteticista', 'Beleza'),
('Renivaldo', 'Engenheiro', 'Infraestrutura'),
('Delei', 'Médico', 'Departamento de Saúde'),
('Tiago', 'Analista de Sistemas', 'Departamento de Informática'),
('Patrício', 'Tesoureiro', 'Departamento de Finanças'),
('José G', 'Digitador', 'Departamento de Licitação'),
('Kerven', 'Streaming de Game', 'Departamento de Esporte');

-- inserindo registros de ponto ficticios
insert into RegistrosPonto(funcionario_id, data, hora_entrada, hora_saida) values
(1, '2026-07-09', '07:00:00', '13:00:00'),
(2, '2026-07-09', '08:30:00', '17:00:00'),
(3, '2026-07-09', '07:00:00', '17:00:00');

select * from Funcionarios;

select * from RegistrosPonto;

