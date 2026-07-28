var musicas = [
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
];

var nomes = [
    "Música 1 - SoundHelix",
    "Música 2 - SoundHelix",
    "Música 3 - SoundHelix"
];

var player = document.getElementById("player");
var indiceAtual = 0;
var modo = "normal";

function tocarMusica(indice){
    indiceAtual = indice;
    player.scr = musicas[indice];
    player.play()
    //atualizar playlist
    var itens = document.querySelectorAll("#lista li");
    itens.forEach(function(item){
        item.classList.remove("active");
    })
    itens[indice].classList.add("active");

    //atualizar faixa atual
    document.getElementById("faixaAtual").textContent = "Tocando agora: " + nomes[indice];

}