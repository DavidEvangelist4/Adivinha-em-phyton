import random

numero_sorteado = random.randint(1,100)
tentativas = 0
rodada = 1
numeros_repetidos = []

print(20 * "*")
print(20 * "*")
print("QUAL O NIVEL VC QUER JOGAR??")
print("1 - NORMAL, 2 - DIFICIO")
print(20 * "*")
nivel = int(input("DIGITE O NIVEL:  "))

if nivel == 1:
    tentativas = 10
elif nivel == 2:  
    tentativas = 3

print(20 * "*")

while rodada <= tentativas:
    print("CHANCE {} de {}".format(rodada, tentativas))
    chute_str = input("DIGITE SEU NÚMERO: ")
    print("Voçê Digitou --->:", chute_str)
    chute = int(chute_str) 
    if (numeros_repetidos.__contains__(chute)):
        print("      REPETIDO")
    else : numeros_repetidos.append(chute)
           
    acerto = chute == numero_sorteado
    maior = chute > numero_sorteado
    menor = chute < numero_sorteado
   
   
    if (acerto):
        print(20 * "*")
        print(         )  
        print ("   Y O U - W I N ")
        print(         ) 
        print("      ヽ༼◉ل͜◉༽ﾉ") 
        print(         )  
        print(20 * "*")  
        break
           
    else:
        if (maior):
            print("Errou ---> O NUMERO É MENOR <--- ")
            print(20 * "*")

        elif(menor):
            print("Errou ---> O NUMERO É MAIOR <--- ")    
            print(20 * "*")
         
        elif(igual):
            print("    NUMERO REPETIDO")
            print(20 * "*")

    rodada = rodada + 1
      
    if (chute) < 1 or chute > 100:
        print("-->>> INVALIDO <<<--")
        print(20 * "*")
        continue
        
    elif (rodada > tentativas):
        print(20 * "*")
        print(         )  
        print ("  Y O U - L O S E ")
        print(         )  
        print("     ¯\_(ツ)_/¯")  
        print(         )  
        print(20 * "*")
        break