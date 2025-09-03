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

    def executar_acao(self, acao):
        if "PEDESTRES" in acao:
            if self.pedestres:
                print("AMBIENTE: Pedestre atravessou com segurança.")
                self.pedestres = False
        elif "CARROS" in acao:
            carros_passando = min(self.carros, 5)
            print(f"AMBIENTE: {carros_passando} carros passaram.")
            self.carros -= carros_passando