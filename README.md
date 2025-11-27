Um simples e divertido jogo de Pedra, Papel e Tesoura desenvolvido em Python, rodando diretamente no terminal. O projeto foi pensado para fins de aprendizado, utilizando conceitos como funções, loops, validação de entrada, manipulação de tela, dicionários e escolhas aleatórias.

⸻

📌 Sobre o Projeto

Este projeto implementa o clássico jogo Jokenpô (Pedra, Papel e Tesoura), onde o jogador enfrenta o computador em partidas ilimitadas até decidir sair.

O código utiliza:
	•	Condicionais para determinar o vencedor;
	•	A biblioteca random para gerar jogadas aleatórias do computador;
	•	A biblioteca os para limpar o terminal durante a execução;
	•	A biblioteca time para criar pequenas pausas que deixam a experiência mais fluida.

⸻

🕹️ Como Funciona

O jogo segue o ciclo:
	1.	O usuário escolhe entre pedra, papel, tesoura ou sair.
	2.	O computador faz uma escolha aleatória.
	3.	O programa exibe o resultado (vitória, derrota ou empate).
	4.	O placar é atualizado automaticamente.
	5.	O jogo continua até o jogador escolher “sair”.

⸻

✨ Funcionalidades
	•	✔️ Limpeza automática da tela a cada rodada
	•	✔️ Validação de entradas
	•	✔️ Placar com vitórias, derrotas e empates
	•	✔️ Sistema de regras completo
	•	✔️ Loop contínuo até o usuário encerrar
	•	✔️ Código simples, organizado e comentado

⸻

🧠 Lógica do Jogo

As regras seguem o padrão:
	•	Pedra ganha de Tesoura
	•	Tesoura ganha de Papel
	•	Papel ganha de Pedra

Caso jogador e computador façam a mesma escolha → Empate.

⸻

🗂️ Tecnologias Utilizadas
	•	Python 3
	•	Bibliotecas padrão:
	•	random
	•	os
	•	time

⸻

🚀 Como Executar o Projeto

1️⃣ Instale o Python (se necessário)

https://www.python.org/downloads/

2️⃣ Baixe ou clone o repositório
git clone https://github.com/SEU-USUARIO/jokenpo-python.git
3️⃣ Entre na pasta do projeto
cd jokenpo-python

4️⃣ Execute o jogo
python jokenpo.py

📁 Estrutura do Projeto
📦 jokenpo-python
 └── jokenpo.py
