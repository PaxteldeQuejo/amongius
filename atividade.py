class Tripulante:
    def __init__(self, nome, cor, chapeu = None, roupinha = None, pet = None):
        self.nome = nome
        self.cor = cor
        self.chapeu = chapeu
        self.roupinha = roupinha
        self.pet = pet
    
    def andar(self):
        print(self.nome, "está andando.")

    def fazer_task(self):
        print(self.nome, "fez uma task.")

    def botao(self):
        print(self.nome, "apertou o botão.")


class Impostor:
    def __init__(self, nome, cor, chapeu = None, roupinha = None, pet = None):
        self.nome = nome
        self.cor = cor
        self.chapeu = chapeu
        self.roupinha = roupinha
        self.pet = pet
    
    def andar(self):
        print(self.nome, "está andando.")

    def fingir_task(self):
        print(self.nome, "fingiu fazer uma task.")

    def matar(self):
        print(self.nome, "matou um dos tripulantes.")

    def ventar(self):
        print(self.nome, "ventou.")

    def sabotar(self):
        print(self.nome, "sabotou.")

    def botao(self):
        print(self.nome, "apertou o botão.")

