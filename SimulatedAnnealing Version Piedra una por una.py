#Se puede hacer búsqueda sistemática o búsqueda con apoyo de la aleatoriedad
#Si se esta en una solucion candidata y se quiere buscar vecinos, aleatoriamente escojo uno, o escojo otro, entonces aqui aplicamos, si
#un vecino es mas malo que el actual, aún así conviene ir al vecino malo, y posteriormente podremos llegar a mejores soluciones
#Si encuentro un vecino malo, aplico loteria y me voy a ese vecino malo.
#Puntos que no son tan buenos como el punto actual son aceptados a veces
#Probabilidad va a ser alta cuando la temperatura es alta, es decir en las etapas iniciales
#Si la solucion mala no es tan mala igual y aumenta la probabilidad de irnos a ella

#La temperatura inicial se le da como un hiperparametro y se le hace descender conforme se progresa
#Una manera de hacerla descender es: temperatura = initial_temperatire/(iteration_number+1)
#Aunque esta temperatura desciende muy violentamente, mejora probabilida de encontrar optimo global

#El criterio para decidir si nos vamos a una solucion peor que la actual es:
#Este criterio es para minimizacion, si quisieramos para maximizacion seria una suma entre objective new y current
#criterion = exp( -(objective(new) – objective(current)) / temperature)

#Estamos tratando de buscar un valor menor al actual, si yo de verdad me encuentro un valor
#menor al actual, siempre me voy a la menor, en ese caso no aplico esta formula.
#Sin embargo esta formula se aplica cuando es mayor que la actual entonces aplicamos la formula de loteria
#para ver si nos vamos ahi o no
#Mientras mayor sea la diferencia entre esa objetctive new y current, entonces mas mala va a ser la solucion  y va a ser mas dificil
#aceptar esa condicion tan mala
#Con temperaturas bajas es mas dificil pasarse a la solucion mas mala

#El algoritmo siempre debe mantener como recuerdo la mejor solucion encontrada hasta el momento
#La mejor no la olvido la guardo en la best solution
#Ya con la temperatura muy baja y viendo que cierta solucion ya no mejoro entonces
#seguir con la solucion mejor que se encontro hasta el momento y seguir mejorando, mejorando hasta donde de la temperatura


#De entrada el algoritmo recibe:
    # una manera o mecanismo de enfriamiento
    # una s0 que es una initial solution
    #T max, que es la temperatura inicial

#Ciclo anidado dentro de otro ciclo
#Ciclo externo es el que modifica la temperatura
#Ciclo interno, que es lo que hace para una temperatura dada:
    #Genera un vecino aleatorio, que puede ser con distribucion normal, aleatoria, gaussiana
    #Hace la E = f(s')-f(s)
    #Si E <= que 0 inmediatamente acepta la E como la solucion, osea sustituye la solucion inicial por la nueva solucion
    #Debido a que significa que f(s') es menor que s, y como queriamos minimizar entonces aceptamos de una vez esa solucion
    #Luego hay un else, que es para aceptar una solucion peor, que seria aceptar una solucion peor con cierta probabilidad

    #Y todo esto lo repite sin cambiar la temperatura hasta alguna condicion de equilibrio, que puede ser hasta cumplir cierto numero de iteraciones
    #o despues de haber probado un cierto numero de iteraciones nunca encontro una solucion que mejorara

    #Cuando ya deja este repeat interno, entonces actualiza la temperatura, es decir la temperatura disminuye, y se repite todo con temperatura mas baja,\
    #Luego el ciclo externo se repite todo hasta que se cumpla cierta condicion, por ejemplo que la temperatura haya descendido a menos que una 
    #temperatura minima

    #Y cuando termina ese repeat pues imprime la mejor solucion encontrada


#La mejor solucion encontrada desde que inicio la busqueda debe de ser guardada en una best solution
#y es va a ser la que se imprimira al final como la best solution

#El vecindario consiste en cambiar aleatoriamente un bit, es decir cambiar una piedra aleatoriamente que esta asignado a uno de los sacos
#es decir cambiarlo a otro saco
#El maximo global de esta funcion 
#Generate a random neighbor va a depender mucho de como representemos la funcion
#Se ocupa tener un vector que tenga el valor de la piedra y la bolsa en la que esta, y como se genera un random neighbor, pues seria cambiar una piedra
#de bolsa a la vez

#-------------------------------------------------------------------
#Librerias Importadas
import random
import math
#-------------------------------------------------------------------
#Estructura para guardar las piedras
#7, 3
#9, 1
#2, 8
#1,3,4,5,8,14,16
set1 = [1]
set2 = [5]
set3 = [16]
bolsas_Piedras = {1: set1, 2: set2, 3:set3}

#-------------------------------------------------------------------
#Parametros:
    #initial_state: 
        #tipo: diccionario, es la bolsa de piedras inicial sin haber pasado por ningun procesamiento
#Funcion:
    #Se encarga de elaborar el algoritmo de simulated annealing para resolver el problema de distribuir de la mejor forma los numeros de la bolsa de piedras
    #en tres sets
#Retorna:
    #La mejor solucion encontrada, es decir donde los tres sets tienen una suma similar de sus elementos, asimismo se retorna el best fitness encontrado
def simulated_annealing(initial_state):
    """Peforms simulated annealing to find a solution"""
    initial_temp = 1000     #Temperatura inicial de simulated annealing
    final_temp = .1         #Temperatura minima, condicion de parada
    alpha = 0.01            #Alpha que se resta para que la temperatura vaya decreciendo
    
    current_temp = initial_temp     #Temperatura actual = inicial

    #Initial Point
    current_state = initial_state.copy()
    best = current_state.copy()
    #Evaluate Initial Point
    best_eval = get_cost(best[1].copy(),best[2].copy(),best[3].copy(), best.copy())
    #current working solution
    curr,curr_eval = best,best_eval

    #Run the algorithm
    while current_temp > final_temp:
        #Take a step
        candidate = get_neighbors(curr[1].copy(),curr[2].copy(),curr[3].copy(), curr.copy())
        
        #Evaluate candidate point
        candidate_eval = get_cost(candidate[1].copy(),candidate[2].copy(),candidate[3].copy(), candidate.copy())

        #Check for new best solution
        if candidate_eval < best_eval:
            #store new best point
            best, best_eval = candidate, candidate_eval
            #report progress
            #falta imprimir el progreso, quizas sirva para comparaciones
        
        #Difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        #Calculate temperature for current epoch
        current_temp -= alpha
        if diff < 0 or random.uniform(0, 1) < math.exp(-diff / current_temp):
            curr, curr_eval = candidate, candidate_eval                

    return [best,best_eval]
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_cost(set1,set2,set3,bolsas_Piedras):
    """Calculates cost of the argument state for your solution."""
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(0,len(set1)-1):
        sum1 += set1[i]
    for i in range(0,len(set2)-1):
        sum2 += set2[i]
    for i in range(0,len(set3)-1):
        sum3 += set3[i]
    
    objective = (sum1 - sum2)**2 + (sum1 - sum3)**2 + (sum2 - sum3)**2
    return objective
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Se da como parametros las soluciones conjuntas
def get_neighbors(set1,set2,set3, bolsas_Piedras):
    """Returns neighbors of the argument state for your solution."""
    #Copiando los sets, la bolsa de piedras, para generar un vecino a partir de una modificacion de la bolsa de piedras que se recibe
    setA = set1.copy()
    setB = set2.copy()
    setC = set3.copy()
    neighbor = {1:setA,2: setB,3: setC}
    
    #Lista de sets
    set_Disponibles_Cambio = ["set1","set2","set3"]

    #Generar un random entre 1 y 3 para ver que conjunto se va a tomar y realizar el cambio
    size = [len(setA),len(setB), len(setC)]
    conjunto_Cambiar = random.randint(1,3)
    while size[conjunto_Cambiar-1] == 0:
        conjunto_Cambiar = random.randint(1,3)
    #Una vez se obtiene el conjunto entonces, hacer un random entre el 0 y ultimo de la lista para ver que casilla del vector se va a elegir para hacer el cambio
    #Y una vez se obtiene la casilla entonces obtener el valor de esa casilla
    #Y luego se elimina del vector
    if conjunto_Cambiar == 1:
        posicion_piedra_Cambiar = random.randint(0,(len(setA)-1))
        piedra = setA[posicion_piedra_Cambiar]
        setA.remove(piedra)
        set_Disponibles_Cambio.remove("set1")
    elif conjunto_Cambiar == 2:
        posicion_piedra_Cambiar = random.randint(0,(len(setB)-1))
        piedra = setB[posicion_piedra_Cambiar]
        setB.remove(piedra)
        set_Disponibles_Cambio.remove("set2")
    else:
        posicion_piedra_Cambiar = random.randint(0,(len(setC)-1))
        piedra = setC[posicion_piedra_Cambiar]
        setC.remove(piedra)
        set_Disponibles_Cambio.remove("set3")
    
    #Se hace un random entre los sets restantes para elegir a cual set ira el neighbor
    set_Destino = random.choice(set_Disponibles_Cambio)
    
    #Se le hace un append al neighbor que resulto ser el elegido    
    if set_Destino == "set1":
        setA.append(piedra)
    elif set_Destino == "set2":
        setB.append(piedra)
    else:
        setC.append(piedra)

    return neighbor

#-------------------------------------------------------------------
#Main
print(simulated_annealing(bolsas_Piedras))




