import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
#Aqui você deve imprimir todo o conteúdo da variável memória
for i in range(0,20):
    print(memoria[i],end="|")
print()
for i in range(20,40):
    print(memoria[i],end="|")
print()
for i in range(40,60):
    print(memoria[i],end="|")
print()
for i in range(60,80):
    print(memoria[i],end="|")
print()
for i in range(80,100):
    print(memoria[i],end="|")
print()
while(opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):
        i=0
        while i < 100:
            if memoria[i] == " ":
                com = i
                j=com+1
                while j < 100:
                    if memoria[j] != " ":
                        final = j
                        i = final
                        espacomem= final - com
                        preenche = tamanho + com
                        if espacomem >= tamanho:
                          for completamem in range(com,preenche):
                            memoria[completamem] = letra
                          i = 100
                          j = 100
                        break
                    j += 1
            i += 1
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            i=0
            while i < 100:
                if memoria[i] == " ":
                    com = i
                    j=com+1
                    while j < 100:
                        if memoria[j] != " ":
                            final = j
                            i = final
                            espacomem = final - com
                            preenche = tamanho + com
                            if espacomem == tamanho:
                              for completamem in range(com,preenche):
                                memoria[completamem] = letra
                              i = 100
                              j = 100
                            break
                        j += 1
                i += 1
        else:
            if(opcao == 3):
              #Implemente aqui a lógica da pior escolha
              i=0
              maior = 0
              comeco = 0
              while i < 100:
                  if memoria[i] == " ":
                      com = i
                      j=com+1
                      while j < 100:
                          if memoria[j] != " ":
                              final = j
                              i = final
                              espacomem = final - com
                              preenche = tamanho + com
                              if espacomem > maior:
                                comeco = com
                                maior = espacomem
                              break
                          j += 1
                  i += 1
              preenche = tamanho + comeco
              if maior >= tamanho:
                for completamem in range(comeco,preenche):
                  memoria[completamem] = letra
          
    # Aqui você deve imprimir todo o conteúdo da variável memória
                  
    for i in range(0,20):
        print(memoria[i],end="|")
    print()
    for i in range(20,40):
        print(memoria[i],end="|")
    print()
    for i in range(40,60):
        print(memoria[i],end="|")
    print()
    for i in range(60,80):
        print(memoria[i],end="|")
    print()
    for i in range(80,100):
        print(memoria[i],end="|")
    print()