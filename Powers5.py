base = 5
numero_potencias = 1000
lista_numeros = []

for i in range(0, numero_potencias):
    lista_numeros.append(list(str(base**i)))
while(True):
    mostrar_columna = input("Ingrese el numero de digito que quiera mostrar(empezando en 1)")
    if(mostrar_columna == -1):
        break;
    freq = 0
    lista_secuencia = []
    print("\n")
    for i in range(1, numero_potencias-1):
        aux = len(lista_numeros[i]) - int(mostrar_columna)
        if(aux>=0):
            lista_secuencia.append(lista_numeros[i][aux])
            if(i+freq < numero_potencias and lista_numeros[i][aux] == lista_secuencia[0] and freq!= 0):
                    switch = True
                    cont_secuencia = 1
                    for j in range(i+1, i+freq):
                        aux = len(lista_numeros[j]) - int(mostrar_columna)
                        if(lista_numeros[j][aux] != lista_secuencia[cont_secuencia]):
                            switch = False
                        cont_secuencia = cont_secuencia + 1

                    if(freq == 1):
                        cont_iguales = 0
                        for j in range(i,i+10):
                            aux1 = len(lista_numeros[j]) - int(mostrar_columna)
                            print(aux1)
                            print(j)
                            if(aux1>=0):
                                if(lista_numeros[i][aux] == lista_numeros[j][aux1]):
                                    cont_iguales= cont_iguales+1
                        if(cont_iguales==10):
                            lista_secuencia.pop(freq)
                            break;

                    elif(switch):
                        lista_secuencia.pop(freq)
                        break;

            freq = freq + 1


    print(mostrar_columna)
    print(lista_secuencia)
    print(freq)
