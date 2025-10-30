from paquete.funciones import *

centros_logisticos = ["Buenos Aires", "San Juan", "Jujuy", "Neuquén"]

insumos = ["Guantes descartables", "Mascarillas quirúrgicas", "Jeringas",
           "Alcohol en gel", "Test rápidos"]

matriz_stock = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

venta_insumos = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]
        
while True:
    print("Menú de opciones")

    print("[1] Cargar stock de insumos")
    print("[2] Mostrar centros con más de 10000 unidades en stock total")
    print("[3] Mostrar insumos con más de 7000 unidades en stock total")
    print("[4] Mostrar centro con mayor cantidad de cada insumo")
    print("[5] Registrar venta de insumos")
    print("[6] Mostrar informe de ventas por centro (ordenado de mayor a menor)")
    print("[7] Mostrar informe de ventas por insumo en cada centro (ordenado de menor a mayor)")
    print("[8] Mostrar informe de reposición de stock")
    print("[9] Porcentaje de stock de cada insumo respecto al total")
    print("[10] Salir del programa")

    opcion = int(input("Elige una opción: "))

    if opcion == 10:
        break
    else:
        match opcion:
            case 1:
                print("CENTROS: Buenos Aires, San Juan, Jujuy, Neuquén")

                centro = input("Elige un centro: ")
                for i in range(len(centros_logisticos)):
                    if centro == centros_logisticos[i]:
                        print("Centro válido")

                        print("INSUMOS: Guantes descartables, Mascarillas quirúrgicas," \
                            " Jeringas, Alcohol en gel, Test rápidos")
                                    
                insumo = input("Elige un insumo: ")     

                for i in range(len(insumos)):
                    if insumo == insumos[i]:
                        print("Insumo válido")

                        cantidad = int(input("Ingresa la cantidad a cargar: "))

                        cargar_insumos(centro, insumo, cantidad, matriz_stock)
                        mostrar_matriz_stock(matriz_stock)
            case 2:
                mostrar_centros_mas_10000_unidades_total(matriz_stock)
            case 3:
                mostrar_insumos_mas_7000_unidades_stock_total(insumos,
                                                              matriz_stock)
            case 4:
                print("INSUMOS: Guantes descartables, Mascarillas quirúrgicas," \
                      " Jeringas, Alcohol en gel, Test rápidos")
                insumo = input("Elige un insumo: ")

                for i in range(len(insumos)):
                    if insumo == insumos[i]:
                        print("Insumo válido")

                        mostrar_centro_con_mayor_cant_insumos(centros_logisticos,
                                                            insumo,
                                                            matriz_stock)
            case 5:
                print("CENTROS: Buenos Aires, San Juan, Jujuy, Neuquén")

                centro = input("Elige un centro: ")
                for i in range(len(centros_logisticos)):
                    if centro == centros_logisticos[i]:
                        print("Centro válido")

                        print("INSUMOS: Guantes descartables, Mascarillas quirúrgicas," \
                            " Jeringas, Alcohol en gel, Test rápidos")
                                            
                        insumo = input("Elige un insumo: ")     

                for i in range(len(insumos)):
                    if insumo == insumos[i]:
                        print("Insumo válido")

                        cantidad = int(input("Ingresa la cantidad que vendiste: "))

                        registrar_venta_de_insumos(venta_insumos,
                                                centro,
                                                insumo,
                                                cantidad,
                                                matriz_stock)
            case 6:
                print("CENTROS: Buenos Aires, San Juan, Jujuy, Neuquén")
                informar_ventas_por_centro(venta_insumos)
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass