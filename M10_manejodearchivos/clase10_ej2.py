import sys


if len(sys.argv)==2:
    import datetime
    import os
    marcadeTiempo= datetime.datetime.now()
    marcadeTiempo= int(datetime.datetime.timestamp(marcadeTiempo))

    llovio = sys.argv[1]
    Temperatura = input('Ingrese la temperatura en grados centigrados')
    Humedad = input ('Ingrese el porcentaje de humedad')    

    linea = str(marcadeTiempo) + ',' + Temperatura + ',' + Humedad + ',' + llovio

    registro_lluvia = open('clase10_ej2.csv','a')
    registro_lluvia.write(linea+'\n')
    registro_lluvia.close()
else:
    print('Se ingresó un numero de variables incorrecta')  
