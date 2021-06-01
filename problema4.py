"""
Como ordenar el proceso de vacunacion
Con el n de privilegiar la inmunidad de los sectores mas susceptibles a sufrir sntomas graves de
COVID19, se le pide organizar el orden de vacunacion de una comunidad de nativos indgenas del
Amazonas. La informacion disponible de la poblacion es sumamente rudimentaria y se reduce a una
serie de anotaciones donde se indican comparaciones de edad entre los nativos. Especcamente, se
tiene para cada nativo al menos una comparacion con otro nativo, donde se indica cual de los dos es
mayor. Agregado a esto, se tiene conocimiento de que algunos registros son incorrectos, lo que puede
llevar a situaciones donde un nativo es simultaneamente mayor y menor que otro. En base a esto, ud.
debe construir un sistema que entregue todas las maneras en que es posible ordenar a los nativos de
mayor a menos prioridad de vacunacion, en base a sus edades. Ademas, si detecta anomalas en la
informacion, como la descrita anteriormente, debe indicar aquellos nativos que presentan problemas en
sus registros.
Para construir el sistema, programe un algoritmo que reciba una lista de tuplas, donde cada tupla
codica la relacion de edad entre dos nativos (cada nativo es identicado con un numero natural
unico). Especcamente, cada tupla codica la relacion A > B, donde A de es el primer elemento de
la tupla y B el segundo. En el caso que sea posible generar ordenes de vacunacion consistentes, la
salida del algoritmo debe consistir en una lista de listas de enteros, donde cada una presenta un posible
orden en que deben realizarse las vacunaciones y cada elemento de la lista representa a un nativo. En
caso de no existir ordenes posibles, su algoritmo debe retornar una lista de enteros, que contenga los
identicadores de los nativos que presentan inconsistencias en sus registros.
Un ejemplo de ejecucion del algoritmo es el siguiente:
Codigo
relaciones = [(0,6),(1,2),(1,4),(1,6),(3,0),(3,4),(5,1),(7,0),(7,1)]
resultado = ordenes_vacunacion(relaciones)
print(resultado)
print()
relaciones = [(0,6),(1,2),(1,4),(1,6),(3,0),(3,4),(5,1),(6,3),(7,0),(7,1)]
resultado = ordenes_vacunacion(relaciones)
print(resultado)
6
Salida
[3, 5, 7, 0, 1, 2, 4, 6]
[3, 5, 7, 0, 1, 2, 6, 4]
[3, 5, 7, 0, 1, 4, 2, 6]
[3, 5, 7, 0, 1, 4, 6, 2]
[3, 5, 7, 0, 1, 6, 2, 4]
[3, 5, 7, 0, 1, 6, 4, 2]
[3, 5, 7, 1, 0, 2, 4, 6]
[3, 5, 7, 1, 0, 2, 6, 4]
[3, 5, 7, 1, 0, 4, 2, 6]
[3, 5, 7, 1, 0, 4, 6, 2]
...
[0, 3, 6]
"""
def ordenes_vacunacion(relaciones):
    lista_p=[]
    #ordeno duplas
    for duplas in relaciones:
        if duplas[0] not in lista_p:
            lista_p.append(duplas[0])
        if duplas[1] not in lista_p:
            lista_p.append(duplas[1])
    lista_p=sorted(lista_p)
    global numero
    numero=0
    lista_dato=[]
    #creo lsita de duplas y valido si estan correcto sus datos
    for p in lista_p:
        aux_d=list()
        for duplas in relaciones:
            if(p==duplas[0]):
                aux_d.append([duplas,duplas[0]>duplas[1]])
        lista_dato.append([p,aux_d])
    lista_orden=[]
    #creo lista con datos correctos 
    lista_orden.append(list())
    #creo lista con datos incorrectos
    lista_orden.append(list())
    for dato in lista_dato:
        if(len(dato[1])>0):
            for dupla in dato[1]:
                if(dupla[1]==True):
                    lista_orden[0].append(dato[0])
                else:
                    lista_orden[1].append(dato[0])
                break
                    
        else:
            lista_orden[1].append(dato[0])
    #validar si es correcta
    global cont
    cont=0
    lista_dato_m=[]
    for dato in lista_dato:
        if(len(dato[1])>0):
            global num
            num=dato[1][0][0][1]
            cont=0;
            #si se crea un ciclo es posible que sea una data erronea
            #con lo cual guardo los valores que genera el bucle 
            while (cont<50 and cont!=-10):
                for d in lista_dato:
                    if(len(d[1])>0):
                        aux1=d[0]
                        if(aux1==num):
                            num=d[1][0][0][1]
                            if num is not lista_dato_m:
                                lista_dato_m.append(num)
                            if aux1 is not lista_dato_m:
                                lista_dato_m.append(aux1)
                            cont+=3            
                if(cont<=0):
                    cont-=1
                if(cont==50):
                    break
            #si no se genero bucle muestro datos   
            if(cont==-10): 
                return lista_orden
            #si se genero bucle muestro numeros que generan el bucle
            if(cont>10):
                lista_dato_m=sorted(set(lista_dato_m))
                return lista_dato_m
             


relaciones = [(0,6),(1,2),(1,4),(1,6),(3,0),(3,4),(5,1),(7,0),(7,1)]
resultado = ordenes_vacunacion(relaciones)
print(resultado)
print()
relaciones = [(0,6),(1,2),(1,4),(1,6),(3,0),(3,4),(5,1),(6,3),(7,0),(7,1)]
resultado = ordenes_vacunacion(relaciones)
print(resultado)
