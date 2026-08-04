// lista inicial de produtos disponiveis
let produtos = [
    {nome: "Costela", precoKg: 39.90},
    {nome: "Alcatra", precoKg: 59.90},
    {nome: "Fraldinha", precoKg: 49.90}
];

// carrinho e historico de compras
let carrinho = [];
let total = 0;
let historico = [];

// funcao para renderizar os produtos na tela
function renderizarProdutos() {
    const lista = document.getElementById("lista-produtos");

    lista.innerHTML = "";

    produtos.forEach((p, index) => {
        const div = document.createElement("div");
        div.className = "produto";
        div.innerHTML = `
            <span>${p.nome}</span>
            <span>R$ ${p.precoKg.toFixed(2)}/kg</span>
            <input type="number" id="qtd-${index}" placeholder="Kg" min="0.1" step="0.1">
            <button onclick="adicionarCarrinho('${p.nome}', ${p.precoKg}, 'qtd-${index}')">Adicionar</button>
        `;
        lista.appendChild(div);
    });

}


//funcao de cadastrar novo produto
function cadastrarProduto() {
    const nome = document.getElementById("nome-produto").value.trim();

    const preco = parseFloat(document.getElementById("preco-produto").value);

    //validacao de dados
    if (!nome || isNaN(preco) || preco <= 0) {
        alert("Informe nome e preço válidos!");
        return;
    }

    //adicionar novo produto ao array(lista)
    produtos.push({nome, precoKg: preco});
    renderizarProdutos();

    //limpar os campos do formulario
    document.getElementById("nome-produto").value = "";
    document.getElementById("preco-produto").value = "";
}

//funcao para dadicionar o produto ao carrinho
function adicionarCarrinho(produto, precoKg, inputId) {
    const qtd = parseFloat(document.getElementById(inputId).value);

    if (isNaN(qtd) || qtd <= 0) {
        alert("Informe a quantidade em Kg!");
        return;
    }

    const precoTotal = precoKg * qtd;
    carrinho.push({produto, qtd, precoTotal});
    total += precoTotal;
    atualizarCarrinho();
    document.getElementById(inputId).value = "";
}

//funcao para atualizar o carrinho na tela
function atualizarCarrinho(){
    const lista = document.getElementById("lista-carrinho");
    lista.innerHTML = "";
    carrinho.forEach((item, index) => {
        const li = document.createElement("li");

        li.textContent = `${item.qtd}kg de ${item.produto} - R$ ${item.precoTotal.toFixed(2)}`;

        // botao remover item
        const btn = document.createElement("button");
        btn.textContent = "Remover";
        btn.className = "remover";
        btn.onclick = () => removerItem(index);
        li.appendChild(btn);
        lista.appendChild(li);
    });
    document.getElementById("total").textContent = `Total: R$ ${total.toFixed(2)}`;
}