def calcular_totales (matriz: list)-> list:
    '''
    Función que realiza la suma de totales de camisetas en cada deposito
    recibe como parámetro una matriz
    retorna una lista
    '''
    
    lista_totales = [0] * len(matriz)
    
    for i in range(len(matriz)):
        suma = 0
        
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
            
            lista_totales[i] += suma
    
    return lista_totales

def estimar_stock(lista_uno: list, lista_dos: list, limite: int) -> None:
    
    '''
    Función para estimar el stock
    Recibe como parámetro: Lista de totales, lista ubicación, limite
    retorna un mensaje con la información requerida
    
    
    '''
    for i in range(len(lista_uno)):
        if lista_uno [i] > limite:
            
            print(f"En el deposito de '{lista_dos[i]}', Hay mas de {limite} camisetas.")

def encontrar_maximo (lista_uno, lista_dos, matriz: list)-> list:
    
    '''
    Función que se encarga de encontrar la cantidad maxima de camisetas por equipo
    recibe como parámetros una matriz y dos lista
    retorna una lista
    '''
    
    maximo = []
    
    for j in range(len(lista_dos)):
        maximo = matriz[0][j]
        deposito_maximo = lista_uno[0]
        
    
        for i in range(len(matriz)):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                deposito_maximo = lista_uno[i]
        
        maximo[j][0] = lista_dos[j]
        maximo[j][1] = maximo
        maximo[j][2]= deposito_maximo
    
    
    return maximo
    
    