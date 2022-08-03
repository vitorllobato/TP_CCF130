from pickle import FALSE, TRUE

N = int(input())
S1 = str(input().replace(" ",""))
S2 = str(input().replace(" ",""))
SS = [0 for s in range(N)]
OPER = str(input().upper())
vet = OPER.split(" ")
resultado = [0 for v in range(N)]

if N < 1001: #Se o número de entradas for menor ou igual a 1000.
    
    for i in range (len (S1)):#Testa se os números recebidos são 0's e 1's no S1.
        if S1[i]=="1" or S1[i]=="0": ##Testa se os números recebidos são 0's e 1's.
            viavel1 = TRUE
        
        else: #Testa se os números recebidos são 0's e 1's e encerra o 'for' se forem diferentes.
            viavel1 = FALSE
            break
    
    for i in range (len (S2)):#Testa se os números recebidos são 0's e 1's no S2.
        if S2[i]=="1" or S2[i]=="0": ##Testa se os números recebidos são 0's e 1's.
            viavel2 = TRUE
        
        else: #Testa se os números recebidos são 0's e 1's e encerra o 'for' se forem diferentes.
            viavel2 = FALSE
            break
    
    if len(S1)==len(S2): #Se o tamanho das entradas S1 e S2 FOREM iguais.
    
        if len(S1)==N: #Se o tamanho das entradas FOREM iguais a "N".

            if viavel1 == TRUE and viavel2 == TRUE: #Dá continuidade no programa se os números inseridos forem 0 ou 1.
                
                if len(vet) == 3: #Se houver apenas um operador lógico. (Os casos de operação entre S1 e S2 serão tratados antes dos casos de repetição.)
                    if vet[0] != vet[2]:
                        if OPER == "S2 OR S1" or OPER == "S1 OR S2": #Caso "OR" para S1+S2.
                            for i in range(N):
                                if S1[i] == "1" or S2[i] == "1":
                                    resultado[i] = 1
                    
                        elif OPER == "S1 NOR S2" or OPER == "S2 NOR S1":#Caso "NOR" para S1+S2.
                            resultado = [1 for v in range(N)]
                            for i in range(N):
                                if S1[i] == "1" or S2[i] == "1":
                                    resultado[i] = 0

                        elif OPER == "S2 XOR S1" or OPER == "S1 XOR S2": #Caso "XOR" para S1+S2.
                            for i in range(N):
                                if S1[i] == "1" and S2[i] == "0":
                                    resultado[i] = 1
                                elif S1[i] == "0" and S2[i] == "1":
                                    resultado[i] = 1
                                elif S1[i] == "0" and S2[i] == "0":
                                    resultado[i] = 0
                                elif S1[i] == "1" and S2[i] == "1":
                                    resultado[i] = 0

                        elif OPER == "S2 AND S1" or OPER == "S1 AND S2": #Caso "AND" para S1+S2.
                            for i in range(N):
                                if S1[i] == "1" and S2[i] == "1":
                                    resultado[i] = 1

                        elif OPER == "S2 NAND S1" or OPER == "S1 NAND S2": #Caso "NAND" para S1+S2.
                            resultado = [1 for v in range(N)]
                            for i in range(N):
                
                                if S1[i] == "1" and S2[i] == "1":
                                    resultado[i] = 0

                        elif OPER == "S1 MOR S2": #Caso "MOR" para S1+S2. 
                            for i in range(N):
                                if S1[i] == "0" or S2[i] == "1":
                                    resultado[i] = 1
                        elif OPER == "S2 MOR S1": #Caso "MOR" para S2+S1.
                            for i in range(N):
                                if S2[i] == "0" or S1[i] == "1":
                                    resultado[i] = 1
                    
                    elif vet[0]==vet[2]: #Casos com S1+S1 e S2+S2
                        
                        if vet[1] == "OR" or vet[1] == "AND": #Casos de OR e AND com termos iguais.
                        
                            if vet[0] == "S1":
                                resultado = S1[:]
                            elif vet[0] == "S2":
                                resultado = S2[:]
                        
                        elif vet[1] == "NAND" or vet[1] == "NOR": #Casos de NOR e NAND com termos iguais.

                            if vet[0] == "S1":
                                for i in range(N):
                                    if S1[i] == "0":
                                        resultado[i] = 1
                                    elif S1[i] == "1":
                                        resultado[i] = 0

                            elif vet[0] == "S2":
                                for i in range(N):
                                    if S2[i] == "0":
                                        resultado[i] = 1
                                    elif S2[i] == "1":
                                        resultado[i] = 0

                        elif vet[1] == "XOR": #Casos de XOR com termos iguais.
                            resultado=resultado[:]
                       
                        elif vet[1] == "MOR": #Casos de MOR com termos iguais.
                            resultado = [1 for i in range(N)]

                                
                    print(*resultado,sep='')
                
                elif len(vet) == 5: #Se houverem dois operadores lógicos.    
                    print ("Sucesso")
            
            else: #Encerra o programa caso os números não forem 0 ou 1.
                print("ERRO") #Encerra o programa caso os números não forem 0 ou 1.
        
        else: #Se o tamanho das entradas NÃO FOREM iguais de "N".
            print("ERRO")
    
    else: #Se o tamanho das entradas S1 e S2 NÃO FOREM iguais.
        print ("ERRO")

else:
    print ("ERRO")