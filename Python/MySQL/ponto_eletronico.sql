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

-- ver registro de ponto de um funcionario especifico
select f.nome, r.data, r.hora_entrada, r.hora_saida from RegistrosPonto r
join Funcionarios f on r.funcionario_id = f.id where f.nome='Guilherme';

-- calcular horas trabalhadas por dia
select f.nome, r.data, timediff(r.hora_saida, r.hora_entrada) as Horas_Trabalhadas from RegistrosPonto r
join Funcionarios f on r.funcionario_id = f.id;

-- verificar quantos funcionarios trabalharam mais de 8 horas
select f.nome, r.data, timediff(r.hora_saida, r.hora_entrada) as Horas_Trabalhadas from RegistrosPonto r
join Funcionarios f on r.funcionario_id = f.id where timediff(r.hora_saida, r.hora_entrada) > '08:00:00';

-- contar quantos registros de ponto existem no banco
select count(*) as Total_Registros from RegistrosPonto;

