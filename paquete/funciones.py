def cargar_insumos(centro: str,
                   insumo: str,
                   cantidad: int,
                   matriz_stock: list) -> None:
    
    match centro:
        case "Buenos Aires":
            fila = 0
        case "San Juan":
            fila = 1
        case "Jujuy":
            fila = 2
        case "Neuquén":
            fila = 3

    match insumo:
        case "Guantes descartables":
            columna = 0
        case "Mascarillas quirúrgicas":
            columna = 1
        case "Jeringas":
            columna = 2
        case "Alcohol en gel":
            columna = 3
        case "Test rápidos":
            columna = 4

    matriz_stock[fila][columna] += cantidad
    

def mostrar_matriz_stock(matriz_stock: list) -> None:

    for i in range(len(matriz_stock)):
        for j in range(len(matriz_stock[i])):
            print(matriz_stock[i][j], end=" ")
        print()


def mostrar_centros_mas_10000_unidades_total(matriz_stock: list) -> None:

    suma_lista = [0, 0, 0, 0]

    for i in range(len(matriz_stock)):
        for j in range(len(matriz_stock[i])):
            suma_lista[i] += matriz_stock[i][j]

    print(suma_lista)

    print("Los centros que tienen más de 10000 unidades de stock en total son:")
    for i in range(len(suma_lista)):
        if suma_lista[i] > 10000:
            match i:
                case 0:
                    print("Buenos Aires")
                case 1:
                    print("San Juan")
                case 2:
                    print("Jujuy")
                case 3:
                    print("Neuquén")


def mostrar_insumos_mas_7000_unidades_stock_total(insumos: list,
                                                  matriz_stock: list) -> None:
    
    suma_lista = [0, 0, 0, 0, 0]

    for i in range(len(matriz_stock)):
        for j in range(len(matriz_stock[i])):
            suma_lista[j] += matriz_stock[i][j]
            
    for i in range(len(suma_lista)):
        if suma_lista[i] > 7000:
            print(f"El insumo {insumos[i]} tiene más de 7000 unidades en stock")
