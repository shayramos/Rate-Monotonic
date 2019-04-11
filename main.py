from processos import Process

def main():
    processList = open("archiveProcess.txt").readlines()
    if not processList:
        print("O arquivo está vazio!")
    else:
        print("encontrei o arquivo")
        #qntprocess = len(processList)
        #print(qntprocess)
        print(processList)
        listObj=[]
        for i in processList:
            p = Process(None, None, None, None)
            p.id = i.split(' ')[0]
            p.executionTime = i.split(' ')[1]
            p.deadline = i.split(' ')[2]
            p.periodo = i.split(' ')[3]
            listObj.append(p)

        #quanto menor o periodo, maior a prioridade
        #considerar maior prioridade 1
        listObj_ordenado = sorted(listObj, key=Process.getPeriodo)
        print(listObj_ordenado[0].id)
        print(listObj_ordenado[1].id)

        cont=1
        for i in listObj_ordenado:
            i.setPrioridade(cont)
            cont=cont+1

        print(listObj_ordenado[0].prioridade)
        print(listObj_ordenado[1].prioridade)
main()