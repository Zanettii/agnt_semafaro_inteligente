import random
class Ambiente:
    def __init__(self):
        self.carros = 0
        self.pedestres = False

    def atualizar(self, ciclo_atual):
        if ciclo_atual <= 10:
            self.carros += random.randint(2, 5)
        else:
            self.carros += random.randint(0, 2)
        if not self.pedestres and random.random() < 0.3:
            self.pedestres = True 

    def executar_acao(self, acao, ciclo_atual):
        vazao_do_ciclo = 0
        if ciclo_atual <= 10: 
            vazao_do_ciclo = 4
        else:
            vazao_do_ciclo = 7
        if "CARROS" in acao:
            carros_passando = min(self.carros, vazao_do_ciclo)
            print(f"AMBIENTE: {carros_passando} carros passaram (Vazão do ciclo: {vazao_do_ciclo}).")
            self.carros -= carros_passando
        elif "PEDESTRES" in acao:
            if self.pedestres:
                print("AMBIENTE: Pedestre atravessou com segurança.")
                self.pedestres = False