class SemaforoAgente:
    def __init__(self):
        self.estado = "VERDE_CARROS"
        self.tempo_no_estado_atual = 0

        self.historico_trafego = []
        self.modo_operacao = "NORMAL"
        self.parametros = {
            "NORMAL": {'pedestre_espera_max': 3, 'min_tempo_pedestre': 2},
            "RUSH_HOUR": {'pedestre_espera_max': 5, 'min_tempo_pedestre': 2}
        }

    def analisar_padroes(self):
        if len(self.historico_trafego) < 5:
            return

        ultimos_ciclos = self.historico_trafego[-5:]
        media_trafego = sum(ultimos_ciclos) / len(ultimos_ciclos)

        if media_trafego >= 3.5:
            if self.modo_operacao != "RUSH_HOUR":
                print("🧠 AGENTE DETECTOU PADRÃO DE RUSH HOUR! MUDANDO ESTRATÉGIA...")
                self.modo_operacao = "RUSH_HOUR"
        else:
            if self.modo_operacao != "NORMAL":
                print("🧠 AGENTE DETECTOU FIM DO RUSH HOUR! VOLTANDO AO NORMAL...")
                self.modo_operacao = "NORMAL"
        
        print(f"AGENTE: Média de tráfego recente: {media_trafego:.2f}. MODO: {self.modo_operacao}")

    def decidir_acao(self, percepcao):
        self.tempo_no_estado_atual += 1
        self.historico_trafego.append(percepcao['carros'])
        
        self.analisar_padroes()

        params_atuais = self.parametros[self.modo_operacao]
        
        if self.estado == "VERDE_CARROS":
            condicao_tempo_esgotado = self.tempo_no_estado_atual >= params_atuais['pedestre_espera_max']
            condicao_pista_livre = percepcao['carros'] == 0
            
            if percepcao['pedestres'] and (condicao_tempo_esgotado or condicao_pista_livre):
                self.tempo_no_estado_atual = 0
                return "ABRIR_PARA_PEDESTRES"
            else:
                return "MANTER_VERDE_CARROS"
        
        elif self.estado == "VERDE_PEDESTRES":
            condicao_tempo_minimo = self.tempo_no_estado_atual >= params_atuais['min_tempo_pedestre']
            
            if condicao_tempo_minimo and (not percepcao['pedestres'] or percepcao['carros'] > 5):
                self.tempo_no_estado_atual = 0
                return "ABRIR_PARA_CARROS"
            else:
                return "MANTER_VERDE_PEDESTRES"

    def atualizar_estado_agente(self, acao):
        if acao == "ABRIR_PARA_PEDESTRES":
            self.estado = "VERDE_PEDESTRES"
        elif acao == "ABRIR_PARA_CARROS":
            self.estado = "VERDE_CARROS"