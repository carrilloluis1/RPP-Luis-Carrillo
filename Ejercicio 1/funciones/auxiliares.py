def inicializar_matriz(numero_filas: int, numero_columnas: int, inicial: any = 0) -> list:
    
    """Esta función Inicializa matrices
    recibe como parámetros el numero de filas, numero de columna y el iniciador
    devuelve una matriz inicializada
    
    """
    
    matriz = []
    
    for _ in range(numero_filas):
        
        fila = [inicial] * numero_columnas
        
        matriz += [fila]
        
    return matriz