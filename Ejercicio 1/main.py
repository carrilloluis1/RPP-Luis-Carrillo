from funciones.auxiliares import *
from funciones.productos import *

lista_depositos = ["Tierra del fuego","Tucuman", "Mendoza", "Bs As", "Misiones", "Santa Fe"]
lista_camisetas = ["Barcelona", "Inter Miami", "PSG", "Manchester City", "Real Madrid"]

ejecutar = True
carga = True

matriz_ejercicio = [[1,2,3,4,5],[500,10,250,350,0,450],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]


while ejecutar == True:
    
    print("Seleccione la opción que desea realizar: ")
    print("1- Obtener existencias.")
    print("2- Mostrar depósitos con mas de 10.000 camisetas.")
    print("3- Mostrar equipos con mas de 5.000 camisetas.")
    print("4-Obtener maxima cantidad de camisetas de cada equipo.")
    
    
    print("6- Salir.")
    
    opcion = input("Ingrese la opción que desea realizar: ")
    
    match opcion:
        
        case "1":
            if carga == True:
                
                matriz_ejercicio = inicializar_matriz(len(lista_depositos), len(lista_camisetas))
                
                for i in range(len(lista_depositos)):
                    for j in range(len(lista_camisetas)):
                        
                        cantidad = input(f"Ingrese la cantidad de camisetas del {lista_camisetas[j]} que hay en {lista_depositos[i]}: ")
                        matriz_ejercicio[i][j] = cantidad
                        
                carga = False
            else:
                
                for i in range(len(matriz_ejercicio)):
                    for j in range(len(matriz_ejercicio[i])):
                        print(f"En {lista_depositos[i]} hay {matriz_ejercicio[i][j]} camisetas del {lista_camisetas[j]}")
        
        case "2":
            # 2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
            
            lista_totales = calcular_totales(matriz_ejercicio)
            
            estimar_stock(lista_totales,lista_depositos,10000)
            
        case '3':
            # 3. Mostrar equipos que hay en stock más de 5.000 camisetas.
            estimar_stock(lista_camisetas,lista_depositos,5000)
        
        case '4':
            # 4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se encuentra.
            lista_maximo = encontrar_maximo(lista_depositos, lista_camisetas, matriz_ejercicio)
        
        case '6':
            ejecutar = False