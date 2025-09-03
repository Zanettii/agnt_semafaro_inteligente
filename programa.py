import time
from ambient import Ambiente
from agent import SemaforoAgente

ambiente = Ambiente()
semaforo = SemaforoAgente()

for i in range(20):
    print(f"\n--- Ciclo {i+1} ---")
    ambiente.atualizar(ciclo_atual=i+1)
    
    percepcao = {'carros': ambiente.carros, 'pedestres': ambiente.pedestres}
    print(f"PERCEPÇÃO: {percepcao['carros']} carros, Pedestre: {percepcao['pedestres']}")

    acao = semaforo.decidir_acao(percepcao)
    print(f"AGENTE DECIDIU: {acao}")
    
    semaforo.atualizar_estado_agente(acao)
    

    ambiente.executar_acao(acao, ciclo_atual=i+1)
    
    time.sleep(2)