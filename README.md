# 🤖 Simulador de Semáforo Inteligente Adaptativo (IA)

Este projeto acadêmico implementa uma simulação em Python de um semáforo inteligente que funciona como um agente de Inteligência Artificial.

O diferencial deste agente é sua **capacidade adaptativa**. Ele não opera com regras fixas, mas monitora o histórico de tráfego para detectar padrões, como horários de pico ("rush hour"). Ao identificar um padrão, o agente ajusta dinamicamente seus parâmetros de decisão para otimizar o fluxo de veículos e pedestres de forma mais eficiente.

---

### 👥 Equipe
* Ana Dantas
* Geisbelly Victoria
* Maria Antonia

---

### 🚀 Como Executar a Simulação

1.  **Ambiente:** Este projeto pode ser executado em um ambiente Python 3 local ou diretamente através do GitHub Codespaces.
2.  **Execução:** Com os arquivos na mesma pasta, abra um terminal e execute o comando:
    ```bash
    python programa.py
    ```
3.  **O que observar:** A simulação rodará por 20 ciclos. Observe no terminal como o agente imprime suas percepções e, mais importante, como ele detecta o início e o fim do "RUSH_HOUR", alterando seu modo de operação e estratégia em tempo real.

---

### 📂 Arquitetura do Projeto

* `ambient.py`: Contém a classe `Ambiente`, responsável por gerenciar o estado do cruzamento. Para tornar a simulação mais realista, a classe simula um "horário de pico" nos ciclos iniciais, gerando um fluxo de carros mais intenso.

* `agent.py`: Contém a classe `SemaforoAgente`, o cérebro da operação.
    * **Memória:** O agente armazena um histórico do volume de tráfego.
    * **Análise de Padrões:** A cada ciclo, ele analisa seu histórico para calcular a média de tráfego recente.
    * **Adaptação:** Com base nessa média, ele pode alternar entre dois modos de operação: "NORMAL" e "RUSH_HOUR". Cada modo possui um conjunto diferente de parâmetros (ex: tempo máximo de espera), tornando-o mais ou menos tolerante a interrupções no fluxo.

* `programa.py`: O script principal que orquestra a simulação, gerenciando o loop de interação entre o Ambiente e o Agente.