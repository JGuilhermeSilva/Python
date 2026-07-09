-- novo eschema chamado copa2026
USE copa2026;

-- Tabela de Seleções
CREATE TABLE Selecoes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(50),
    continente varchar(30)    
);

-- Tabela dos jogadores
CREATE TABLE Jogadores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(50),
    idade int,
    posicao varchar(30),
    selecao_id int,
    foreign key (selecao_id) references selecoes(id)
);

CREATE TABLE Estadios(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(50),
    cidade varchar(50),
    capacidade int
);


-- Tabela de partidas de futebol
CREATE TABLE Partidas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    selecao1_id INT,
    selecao2_id INT,
    estadio_id INT,
    data Date,
    foreign key (selecao1_id) references Selecoes(id),
    foreign key (selecao2_id) references Selecoes(id),
    foreign key (estadio_id) references Estadios(id)
);

-- Tabela de Resultados
CREATE TABLE Resultados (
	id INT AUTO_INCREMENT PRIMARY KEY,
    partida_id int,
    gols_selecao1 int,
    gols_selecao2 int,
    foreign key (partida_id) references Partidas(id)
);

-- inserindo dados
INSERT INTO Selecoes(nome, continente) VALUES
('Brasil', 'América do Sul'),
('Alemanha', 'Europa'),
('Japão', 'Ásia'),
('EUA', 'América do Norte');

INSERT INTO Jogadores(nome, idade, posicao, selecao_id) VALUES
('Neymar Jr', 34, 'Atacante', 1),
('Thomas Muller', 36, 'Meia', 2),
('Takumi Minamino', 31, 'Atacante', 3),
('Christian Pulisic', 27, 'Meia', 4);

INSERT INTO Estadios(nome, cidade, capacidade) VALUES
('MetLife Stadium', 'Nova Jersey', 82500),
('SoFi Stadium', 'Los Angeles', 70000);

INSERT INTO Partidas(selecao1_id, selecao2_id, estadio_id, data) VALUES
(1, 2, 1, '2026-06-15'),
(3, 4, 2, '2026-06-16');

INSERT INTO Resultados(partida_id, gols_selecao1, gols_selecao2) VALUES
(1, 2, 1),
(2, 0, 0);

select * from Selecoes;

select * from Jogadores;

select * from Estadios;

select * from Partidas;

select * from Resultados;

select nome, posicao from Jogadores where selecao_id = 1;

select s1.nome as selecao1, s2.nome as selecao2, e.nome as estadio, p.data from Partidas p
join Selecoes s1 on p.selecao1_id = s1.id
join Selecoes s2 on p.selecao2_id = s2.id
join Estadios e on p.estadio_id = e.id;



