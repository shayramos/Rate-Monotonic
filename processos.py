class Process:
    def __init__(self, id, executionTime, deadline, periodo):
        self.id = id
        self.executionTime = executionTime
        self.deadline = deadline
        self.prioridade = None
        self.periodo = periodo
        self.startTime = 0
        self.executedTime = 0

    def excutar(self, id):
        print("Executando")

    def emEspera(self):
        print("Em espera")