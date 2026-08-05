
// Configurações básicas da API do Hospital
const API_URL = 'https://randomuser.me/api/'; // Substitua pela URL real do hospital
const INTERVALO_ATUALIZACAO = 5000; // Tempo em milissegundos (5 segundos)

let ultimoNomeChamado = "";

// Função para simular o som do painel (Bip) usando o próprio navegador
function tocarAlertaSonoro() {
    const context = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = context.createOscillator();
    const gainNode = context.createGain();

    oscillator.type = 'sine';
    oscillator.frequency.setValueAtTime(587.33, context.currentTime); // Nota Ré (D5)
    oscillator.frequency.setValueAtTime(880, context.currentTime + 0.1); // Nota Lá (A5)

    gainNode.gain.setValueAtTime(0.1, context.currentTime);

    oscillator.connect(gainNode);
    gainNode.connect(context.destination);

    oscillator.start();
    oscillator.stop(context.currentTime + 0.3);
}

// Função principal que busca os dados da API do hospital
async function buscarDadosPainel() {
    try {
        /* 
           QUANDO A API ESTIVER PRONTA:
           Descomente as linhas abaixo para puxar os dados reais:
        */
        // const resposta = await fetch(API_URL, { headers: { 'Authorization': 'Bearer SEU_TOKEN' } });
        // const dados = await resposta.json();

        // --- SIMULAÇÃO DE DADOS (Remover quando integrar com a API real) ---
        const API_URL = "https://randomuser.me/api/";

        const resposta = await fetch(API_URL);
        const resultado = await resposta.json();

        ///////////////////
        
        const pessoa = resultado.results[0]; 

        // Transforma o formato deles no seu formato { nome, sala }
        const dados = {
            nome: `${pessoa.name.first} ${pessoa.name.last}`,
            sala: `Consultório ${Math.floor(Math.random() * 5) + 1}` // Sorteia uma sala de 1 a 5
        };
/*
        const listaSimulada = [
            { nome: "Carlos Alberto S.", sala: "Consultório 3" },
            { nome: "Maria Eduarda F.", sala: "Triagem 1" },
            { nome: "João Pedro M.", sala: "Raio-X" }
        ];
        // Escolhe um paciente aleatório da simulação para simular a mudança
        const dados = listaSimulada[Math.floor(Math.random() * listaSimulada.length)];
        // ------------------------------------------------------------------
 */
        // Verifica se o paciente mudou para disparar o alerta visual e sonoro
        if (dados.nome !== ultimoNomeChamado) {
            ultimoNomeChamado = dados.nome;

            // Atualiza a tela
            document.getElementById('nome').innerText = dados.nome;
            document.getElementById('sala').innerText = dados.sala;

            // Dispara efeitos
            //////////////////////////////////////tocarAlertaSonoro();
            const elementoPainel = document.getElementById('painel');
            elementoPainel.classList.add('destaque');

            // Remove o efeito de piscar após 1.5 segundos
            setTimeout(() => {
                elementoPainel.classList.remove('destaque');
            }, 1500);
        }

    } catch (erro) {
        console.error("Erro ao buscar dados da API do hospital:", erro);
        document.getElementById('nome').innerText = "Erro de Conexão";
        document.getElementById('sala').innerText = "Verificar TI";
    }
}

// Atualiza o relógio digital no rodapé
function atualizarRelogio() {
    const agora = new Date();
    document.getElementById('relogio').innerText = agora.toLocaleTimeString('pt-BR');
}

// Inicialização do painel ao carregar a página
setInterval(buscarDadosPainel, INTERVALO_ATUALIZACAO);
setInterval(atualizarRelogio, 1000);

// Executa a primeira busca imediatamente ao abrir
buscarDadosPainel();
atualizarRelogio();