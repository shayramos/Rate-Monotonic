# -*- coding: utf-8 -*-

from processos import Process
import math
#from RM_algorithm import RateMonotonic

def calculo(lista):
    
    #Inicialmente calculará o valor para uma única tarefa.
    #Mas deve ser feito para que rode em todas.
    #C_i : tempo de processamento "real"(tempo útil) de uma tarefa i;
    #R_k, R_k+1 : Tempo de resposta calculado nas iterações k e k+1. Chamamos R_k e R_k+1 de "anterior" e "atual" respectivamente;
    
     
     #Calcular o tempo de resposta máximo de cada processo
    for i in lista:
        
        #Declarando variáveis necessárias
        anterior = 0
        atual = 0 

        if(i.prioridade == 0):  # Se for a primeira tarefa (maior prioridade), atual = C0 (C da tarefa de maior prioridade)
            atual  = i.executionTime
            if( atual > i.deadline):  # Se por acaso o C da maior prioridade for maior que seu deadline, retorna falso
                return False

        #Se a prioridade da tarefa não for a maior de todas        
        else:
            anterior =  i.executionTime #Faz R_k = C_i 

        #Esse WHILE calcula os R_k+1 (iterações)
            while(atual <= i.deadline):   #Se por acaso o resultado da última iteração R_k tiver valor  o deadline da tarefa i, então retorna false  
                atual = 0 #Reseta 'atual'
                for j in lista:  #Varrer processos de prioridade maior
                    if (j.prioridade >= i.prioridade): # Se a prioridade for menor, então já percorremos todas tarefas de prioridade
                                                       # maior que a atual(i), ou seja, dá um 'break' no FOR do somatório;
                        break
                    else:
                        #Calcula o somatorio caso não tenha varrido todas as tarefas de maior prioridade
                        atual = atual + (math.ceil(anterior / j.deadline))*j.executionTime   

                atual = atual + i.executionTime #Acrescentando o C_i        
                #print("VALOR atual ",atual, "  ", i.id)

                if(atual > i.deadline):
                    #print("FLAG 1")
                    return False #Caso o valor calculado ultrapasse o valor do deadline;    
    
                if(atual == anterior):  # Caso o valor calculado seja menor que deadline e R_k == R_k+1
                    break
                else:
                    anterior = atual     #Atualiza 'anterior' caso atual não tenha alcançado mesmo valor de 'anterior' 

            
            
    #Se todas as tarefas não extrapolaram os seus respectivos deadlines, entao retorna true
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
            p.executionTime = int(i.split(' ')[1])
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
        
        if(calculo(listObj_ordenado)):
            print("Escalonabilidade factível")
        else:
            print("Escalonabilidade impossivel")
      
main()