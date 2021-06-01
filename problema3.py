"""
Que evaluaciones conviene hacer 
Nadie duda que la etapa universitaria es una de las mas exigentes y cansadoras en la vida, en particular
en esta epoca de pandemia. Uno de los elementos que mas problemas causa es la organizacion del tiempo
de estudio, en particular aquel dedicado al desarrollo de evaluaciones. Con el n de facilitar la vida de
los futuros estudiantes, ud. debera desarrollar un sistema de asignacion de tiempo, que dada una lista
de evaluaciones, su fecha de entrega y su ponderacion en la nota nal, entregue una programacion para
su desarrollo que maximice el promedio de notas. Para esto, puede asumir lo siguiente:
• Cada evaluacion puede desarrollarse durante 1 da.
• No pueden desarrollarse 2 o mas evaluaciones de manera simultanea.
• Cada evaluacion puede entregarse en cualquier da menor o igual al lmite.
• La ponderacion total de las notas puede sumar un numero natural arbitrario.
• Las evaluaciones entregadas reciben nota 1 y las no entregadas nota 0.
Para construir el sistema, programe un algoritmo que reciba una lista de tuplas, donde cada tupla
almacena el nombre de la tarea, los das que restan para su entrega, y la ponderacion que tiene esta
en la nota nal. La salida del algoritmo debe consistir en una lista que presenta el orden en que deben
realizarse las evaluaciones, y en un numero que represente la nota ponderada nal que se obtendra.
Esta se calcula como la suma de la ponderacion de cada evaluacion multiplicado por su nota, dividido
por la suma de las ponderaciones, el valor obtenido se debe aproximar a 2 cifras despues de la coma.
Un ejemplo de ejecucion del algoritmo es el siguiente:
Codigo
evaluaciones = [(Tarea4,9,15),(Control1,2,2),(I1,5,18),(Control3,7,1),
(Control2,4,25),(Taller1,2,20),(Tarea2,5,8),(Tarea3,7,10),
(Taller2,4,12),(Tarea1,3,5)]
orden, nota = programar_evaluaciones(evaluaciones)
print(orden)
print(nota)
Salida
[Tarea2,Taller1,Taller2,Control2,I1,Control3,Tarea3,Tarea4]
"""
import math

def programar_evaluaciones(evaluaciones):
    global notaT
    notaT=0
    #sumo el total de notas
    for j in evaluaciones:
        notaT+=j[2]
    list_r=[]
    #ordeno las duplas
    ordenados=sorted(evaluaciones,key=lambda tarea:tarea[1]);
    for i in range(len(evaluaciones)):
        list_r.append(list())
        for evaluacion in evaluaciones:
          if((i)==evaluacion[1]):
            list_r[i].append(evaluacion)
    list_r.pop(0)
    #reposiciono las tareas si hay dos en el mismo dia,
    #se mueve al tope y si hay una tarea con menor ponderacion
    #hace cambio y repete el ciclo . si no hay lugar antes
    #de la fecha limite con menor ponderacion se elimina
    for r in list_r:
        if(len(r)>1):
            aux=[]
            if(r[0][2]>r[1][2]):
                aux=r[1]
                r.pop(1)
            elif(r[0][2]<r[1][2]):
                aux=r[0]
                r.pop(0)
            else:
                aux=r[1]
                r.pop(1)
            for i in range(aux[1]):
                if(len(list_r[i])==0):
                    list_r[i].append(aux)
                    break
                elif(len(list_r[i])==1):
                    if(list_r[i][0][2]<aux[2]):
                        list_r[i]=list()
                        list_r[i].append(aux)
                        break
    global notaS
    notaS=0
    global notaF
    notaF=0
    list_tarea=[]
    #calculo promedio
    for i in range(len(list_r)-1):
        if(len(list_r[i])==0):
            list_r.pop(i)
        notaS+=list_r[i][0][2]
        list_tarea.append(list_r[i][0][0])
    notaF=round(notaS/notaT,2)               

    return list_tarea,notaF

evaluaciones = [('Tarea4',9,15),('Control1',2,2),('I1',5,18),('Control3',7,1),
                ('Control2',4,25),('Taller1',2,20),('Tarea2',5,8),('Tarea3',7,10),
                ('Taller2',4,12),('Tarea1',3,5)]

programar_evaluaciones(evaluaciones)
orden, nota = programar_evaluaciones(evaluaciones)
print(orden)
print(nota)
