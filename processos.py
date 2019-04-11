class Process:
    def __init__(self, id, executionTime, deadline, periodo):
        self.id = id
        self.executionTime = executionTime
        self.deadline = deadline
        self.periodo = periodo
        self.prioridade = None
        self.startTime = 0
        self.executedTime = 0

    def getPeriodo(self):
        return self.periodo

    def setPrioridade(self, p):
        self.prioridade = p

    def excutar(self, id):
        print("Executando")

    def emEspera(self):
        print("Em espera")