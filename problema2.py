"""
Sopa de letras
Un restaurant especializado en sopas con servicio de delivery promete a sus clientes sopas de letras
personalizadas, donde es posible leer un texto libre elegido por el cliente. Lamentablemente, debido
al exceso de demanda, el servicio de delivery ha tenido problemas para mantener la \integridad" del
texto, por lo que cuando las sopas llegan a los clientes, estas vienen con el texto desordenado. Con el
n de evitar la fuga de clientes, el restaurant ofrece a todos aquellos que hayan tenido problemas, una
sopa gratis, si son capaces de comprobar que no es posible encontrar el texto personalizado.
Para lograr esto, su mision es programar un algoritmo que, dada una matriz de letras mayusculas (lista
de strings, todos del mismo largo, primer string indica la primera la de la matriz) que representa una
vista superior de la sopa de letras, encuentre todas las ocurrencias del texto personalizado considerando
las 8 direcciones. En caso de encontrar ocurrencias, su algoritmo debe retornarlas como una lista de
listas de tuplas, donde cada lista de tuplas contiene las posiciones de los caracteres del texto buscado,
es decir, cada tupla de la lista indica la posicion de un caracter, en formato (la, columna), donde la
coordenada (0,0) corresponde al caracter ubicado en la posicion superior izquierda de la matriz.
Un ejemplo de ejecucion del algoritmo es el siguiente:
Codigo
sopa = ["LAMXB", "AOEYF", "FCHTB", "GFKAR", "POSFD"]
texto = "HOLA"
posiciones = encontrar_ocurrencias(sopa, texto)
print(*posiciones, sep="\n")
Salida
[(2, 2), (1, 1), (0, 0), (0, 1)]
[(2, 2), (1, 1), (0, 0), (1, 0)]
"""
#valido que la posicion que se esta moviendo esta en los
#limites de la matriz
def limite(sopa,x,y):
    return (x<len(sopa) and y<len(sopa[0]) and x>=0 and y>=0)

#giro es una funcion recursiva que busca
#letras en los 8 espacios al rededor de la letra
def giro(sopa,x,y,lis1,lis2,texto,pos):
    global ban
    global x1
    global y1
    ban=0
    x1=x
    y1=y
    #las ocho posiciones posibles dentro de la matriz
    dupla=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,0],[-1,1],[0,1]]
    if(pos<len(texto)):#si llego al final paro ejecucion
        for item in dupla:
            if(limite(sopa,x1+item[0],y1+item[1])):
                if(texto[pos]==sopa[x1+item[0]][y1+item[1]]):
                    lis1.append(texto[pos])
                    lis2.append([x1+item[0],y1+item[1]])
                    giro(sopa,x1+item[0],y1+item[1],lis1,lis2,texto,pos+1)


def encontrar_ocurrencias(sopa, texto):
    global numero
    numero=0
    lis_letraE=[]
    lis_pos=[]
    res=[]
    #busco la primera palabra de la matriz
    for letra in texto:
        for i in range(len(sopa)):
            for j in range(len(sopa[0])):
                 if(letra==sopa[i][j]):
                     if letra not in lis_letraE:
                         #agrego la palabra y llamo a giro
                         lis_letraE.append(letra)
                         lis_pos.append([i,j])
                         giro(sopa,i,j,lis_letraE,lis_pos,texto,1)
                         numero=1
                         break
            if(numero==1):break
        if(numero==1):break
    #ordenos las duplas que se generaron   
    if(len(texto)!=len(lis_letraE)):
        aux=len(lis_letraE)-len(texto)
        global len_p
        len_p=len(texto)
        numero=0
        for i in range(aux+1):
            res.append(list())
            for p in lis_pos:
                if(numero==len_p):break
                res[i].append(p)
                numero+=1
            lis_pos.pop(len_p-1)
            numero=0
        res=res[::-1]
    return res
   
     
sopa = ["LAMXB", "AOEYF", "FCHTB", "GFKAR", "POSFD"]
texto = "HOLA"
posiciones = encontrar_ocurrencias(sopa, texto)
print(*posiciones, sep="\n")


