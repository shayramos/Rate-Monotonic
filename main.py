from processos import Process
import math
#from RM_algorithm import RateMonotonic

def calculo(lista):
    
    #Inicialmente calculará o valor para uma única tarefa.
    #Mas deve ser feito para que rode em todas.
    
    #CONSIDERE UM PROCESSO 'i':
     
     #Calcular o tempo de resposta máximo de cada processo
    for i in lista:
        print("Comecando processo ",i.id)
        if(i.prioridade == 0):  # Se for a primeira tarefa (maior prioridade), atual = C0 (C da tarefa de maior prioridade)
            atual  = i.executionTime
            if( atual > i.deadline):  # Se por acaso o C da maior prioridade for maior que seu deadline, retorna falso
                print("FLAG")
                return False
        #Se a prioridade da tarefa não for a maior de todas        
        else:
            anterior =  i.executionTime #Essas 2 variaveis (anterior e atual) se referem ao R_k e R_k+1
            print("VAlor de anterior ", anterior)
            atual = 0 

        #Esse WHILE calcula os valores do tempo de atraso
            while(atual <= i.deadline):    
                atual = 0 #Reseta 'atual'
                for j in lista:  #Varrer processos de prioridade maior
                    if (j.prioridade >= i.prioridade): # Se a prioridade for menor, então dá um 'break';
                        break
                    else:
                        print("Usando ",j.id)
                        #Calcula o somatorio
                        atual = atual + (math.ceil(anterior / j.deadline))*j.executionTime   

                atual = atual + i.executionTime #Acrescentando o C_i        
                print("VALOR atual ",atual, "  ", i.id)

                if(atual > i.deadline):
                    print("FLAG 1")
                    return False #Caso o valor calculado ultrapasse o valor do deadline;    
    
                if(atual == anterior):  # Caso o valor calculado seja menor que deadline e R_k == R_k+1
                    break
                else:
                    anterior = atual     #Atualiza 'anterior' caso atual não tenha alcançado mesmo valor de 'anterior' 

            
            print("Tarefa ",i.id, " OK ")
    #Se rodou todas as tarefas OK, entao retorna true
    return True    

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
            p.executionTime =int(i.split(' ')[1])
            p.deadline = int(i.split(' ')[2])
            p.periodo = int(i.split(' ')[3])
            listObj.append(p)

        #quanto menor o periodo, maior a prioridade
        #considerar maior prioridade 1
        listObj_ordenado = sorted(listObj, key=Process.getPeriodo)
        for i in listObj_ordenado:
            print(i.id ,i.deadline)
      

        cont=1
        for i in listObj_ordenado:
            i.setPrioridade(cont)
            cont=cont+1
        

        for i in listObj_ordenado:
            print(i.prioridade, i.id)
        
        print(calculo(listObj_ordenado))
      
main()