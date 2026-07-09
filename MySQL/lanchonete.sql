-- novo esquema
USE lanchonete;

create table Produtos(
	id int auto_increment primary key,
    nome varchar(50),
    categoria varchar(30),
    preco decimal(6,2),
    estoque int    
);

create table Clientes(
	id int auto_increment primary key,
    nome varchar(50),
    idade int,
    cidade varchar(50)
);

create table Pedidos(
	id int auto_increment primary key,
    cliente_id int,
    data Date,
    foreign key (cliente_id) references Clientes(id)
);

create table ItensPedido(
	id int auto_increment primary key,
    pedido_id int,
    produto_id int,
    quantidade int,
    foreign key (pedido_id) references Pedidos(id),
    foreign key (produto_id) references Produtos(id)
);


insert into Produtos(nome, categoria, preco, estoque) values
('Hamburguer', 'Salgado', 12.50, 50),
('Coxinha', 'Salgado', 5.00, 100),
('Suco de Laranja', 'Bebida', 6.00, 80),
('Refrigerante 2L', 'Bebida', 8.50, 40),
('Bolo de Chocolate', 'Doce', 15.00, 20);

insert into Clientes(nome, idade, cidade) values
('Guilherme', 23, 'Frei Martinho'),
('Lindomara', 22, 'Frei Martinho'),
('Renivaldo', 23, 'Picuí');

insert into Pedidos(cliente_id, data) values
(1, '2026-07-08'),
(2, '2026-07-08');
    
insert into ItensPedido(pedido_id, produto_id, quantidade) values
(1, 1, 2),
(1, 4, 1),
(2, 5, 1),
(2, 3, 1);


select * from Produtos;

select * from Clientes;

select * from Pedidos;

select * from ItensPedido;

select c.nome as cliente, prod.nome as itens_produtos, p.data from Pedidos p
join Clientes c on p.cliente_id = c.id
join ItensPedido i on p.id = i.pedido_id
JOIN Produtos prod ON i.produto_id = prod.id;