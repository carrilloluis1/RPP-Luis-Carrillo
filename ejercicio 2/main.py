# 2. Generar una función que calcule la suma de las diagonales principal y secundaria de una

def calcular_diagonales(matriz:list)-> int:
    
    if len(matriz) != len(matriz[0]):
        return None
    
    suma_principal = 0
    suma_secundaria = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if i == j:
            
                suma_principal += matriz[i][j]
            
            elif i == (len(matriz)-1):
                suma_secundaria += matriz[i][j]
        
        suma_total = suma_principal + suma_secundaria
    
    return suma_total