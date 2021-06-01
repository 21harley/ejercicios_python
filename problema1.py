"""
Los Cristaloides y su red del metro
Los cristaloides son criaturas aliengenas fascinantes que tienen un nivel de inteligencia similar al de los
humanos, pero presentan una vision particular: pueden distinguir pero no identicar colores. Por
ejemplo, si le muestras dos cuadrados de colores distintos, separados, no sabran decir si se trata del
mismo color o no, pero si le pones uno junto (o parcialmente superpuesto) al otro, sabran con certeza
si es o no el mismo color. Esto les plantea inconvenientes a la hora de leer los planos del metro de
su planeta natal, ya que como todas las lneas son del mismo color, se pierden con frecuencia en las
combinaciones.
Para ayudar a estos seres, su mision es programar un algoritmo que, dada una red de metro, le indique
a los cristaloides el color del cual deben pintar cada una de las lineas para que puedan ubicarse sin
problemas, con la restriccion de que la cantidad de colores utilizados debe ser mnima. La entrada a su
algoritmo seran: i) una lista de listas, donde cada sublista indica las estaciones de una lnea de metro
(cada estacion de la red tiene un identicador unico dado por un numero natural), y ii) un set de
tuplas, donde cada tupla indica una combinacion entre dos lneas de la red. La salida de su algoritmo
debe ser una lista de enteros, donde cada posicion de la lista indica el color (numero natural) asignado
a lnea asociada a ese ndice, es decir, si en la posicion 3 de la lista hay un 5, signica que a la lnea 3
se le asigno el color 5.
Un ejemplo de ejecucion del algoritmo es el siguiente:
Codigo
lineas = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
combinaciones = {(0, 10), (1, 6)}
colores = asignar_colores(lineas,combinaciones)
print(colores)
Salida
[0, 1, 1]
"""

#recorto la linea que no esta super puesta
def recortarV(linea,start,end):
    newLis=[]
    global numero
    numero=0
    for n in linea:
        if(numero>=start):
            newLis.append(n)
        numero+=1
    return newLis

def asignar_colores(lineas,combinaciones):
    listaResultados=[]
    global numeroD
    numeroD=0
    #agrupo las duplas que se intercrusan 
    for duplas in combinaciones:
        lisp=[]
        for linea in lineas:
            global numero
            numero=0
            for iden in linea:
                if(duplas[0]==iden):
                    #evito agrupar numeros que no esta super puesto
                    aux1=recortarV(linea,numero,len(linea)-1)
                    for aux in aux1:
                        lisp.append(aux) 
                if(duplas[1]==iden):
                    #evito agrupar numeros que no esta super puesto
                    aux2=recortarV(linea,numero,len(linea)-1)
                    for aux in aux2:
                        lisp.append(aux) 
                numero+=1
        lisp.sort()
        listaResultados.append(lisp[0])
        numeroD+=1
    #caso cuando la cantidad de duplas es menor a las combinaciones 
    if(len(lineas)!=numeroD):
        if(len(lineas)>numeroD):
             lisp=[]
             for duplas in combinaciones:
                lineasf=recortarV(lineas,numeroD,len(lineas)-1)
                for lineaf in lineasf:
                    for item1 in lineaf:
                        if(duplas[1]==item1):
                            for num in lineaf:
                                lisp.append(num)
                            for linea in lineas:
                                for item in linea:
                                    if(duplas[0]==item):   
                                        for num1 in linea:
                                            if(num1!=item):
                                               lisp.append(num1)

                if(len(lisp)>0):
                    lisp.sort()
                    listaResultados.append(lisp[0])
    #limpio salida
    listaResultados.sort()
    resul=[]
    for aux in listaResultados: resul.append(aux)
    return resul

lineas = [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
combinaciones = {(0, 10), (1, 6) }
colores = asignar_colores(lineas,combinaciones)
print(colores)
