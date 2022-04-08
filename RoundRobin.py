from time import sleep

#leitura do arquivo
with open("processos.txt") as f:
    processos = f.read().splitlines() 

#formatação das strings lidas
for i in range(len(processos)):
    processos[i] =  processos[i].split(";")
    processos[i][1] = int(processos[i][1])

#maior processo
for k in range(len(processos)):
    maior = processos[k][1]
    if processos[k][1] > maior:
        maior = processos[k][1]

#leitura do quantum
quantum = int(input("Digite o número do quantum: "))
contador = quantum 

#Round Robin
while contador < maior:
    for c in range(0,len(processos)):
        if contador < processos[c][1]:
            print("Processo %s em execução por %d segundos...  [%d]/[%d]" % (processos[c][0],quantum,contador,processos[c][1]))
            sleep(quantum)
        elif contador >= processos[c][1]:
            print("Processo %s OK - [%d]/[%d]" % (processos[c][0],processos[c][1],processos[c][1]))
    contador += quantum
print("Processos finalizados com sucesso!")

       
