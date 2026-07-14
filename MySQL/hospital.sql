-- novo esquema chamado hospital
USE hospital;

-- criando a tabela de pacientes
create table Pacientes(
	id int auto_increment primary key,
    nome varchar(50),
    idade int,
    genero varchar(10),
    cidade varchar(50)	
);

-- criando tabela de triagem (protocolo de manchester)
create table Triagem(
	id int auto_increment primary key,
    paciente_id int,
    data Date,
    sintomas varchar(100),
    classificacao varchar(10), -- (vermelho, laranja, amarelo, verde, azul)
    foreign key (paciente_id) references Pacientes(id)
);

-- tabela de atendimentos
create table Atendimentos(
	id int auto_increment primary key,
    triagem_id int,
    medico varchar(50),
    diagnostico varchar(100),
    foreign key (triagem_id) references Triagem(id)
);

insert into Pacientes(nome, idade, genero, cidade) values
('Guilherme', 23, 'Masculino', 'Frei Martinho'),
('Anderson', 33, 'Masculino', 'Uberlândia'),
('Patricio', 22, 'Masculino', 'Frei Martinho'),
('Fátima', 40, 'Feminino', 'Pedra Lavrada'),
('Maria da Guia', 25, 'Feminino', 'Nova Palmeira'),
('Patrícia', 50, 'Feminino', 'Cubati'),
('Fernanda', 19, 'Feminino', 'Cuité');

insert into Triagem(paciente_id, data, sintomas, classificacao) values
(1, '2024-07-13', 'dor no peito intensa', 'vermelho'), -- emergencia
(2, '2026-07-11', 'Febre alta e tosse', 'amarelo'), -- urgente
(3, '2024-07-12', 'Dor de cabeça leve', 'verde'), -- pouco urgente
(4, '2024-07-10', 'Febre leve', 'azul'); -- nao urgente

insert into Atendimentos(triagem_id, medico, diagnostico) values
(1, 'Dr. Hans Chucrute', 'refrigerante em excesso'),
(2, 'Dra. Paula', 'Infecção respiratória'),
(3, 'Dr. Diego Mendes', 'Cafaleia tensional'),
(4, 'Dr. Vânia', 'Cafaleia leve');

-- contar quantos pacientes em cada classificacao
select classificacao, count(*) as total from Triagem group by classificacao;

select p.nome, t.classificacao, a.medico, a.diagnostico from Atendimentos a
join Triagem t on a.triagem_id = t.id
join Pacientes p on t.paciente_id = p.id;

DESCRIBE triagem;