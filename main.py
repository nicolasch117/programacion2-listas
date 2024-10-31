from lista_viajes import ListaViajes
from viajes import Viaje

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE VIAJES ===")
    print("1. Agregar nuevo viaje")
    print("2. Listar todos los viajes")
    print("3. Calcular total de precios")
    print("4. Calcular promedio de precios")
    print("5. Ver viaje más costoso")
    print("6. Salir")
    return input("Seleccione una opción: ")

def ingresar_viaje():
    print("\n--- Ingreso de nuevo viaje ---")
    try:
        origen = input("Ingrese ciudad de origen: ")
        destino = input("Ingrese ciudad de destino: ")
        fecha = input("Ingrese fecha (YYYY-MM-DD): ")
        precio = float(input("Ingrese precio: "))
        
        return Viaje(origen, destino, fecha, precio)
    except ValueError as e:
        print(f"Error al ingresar datos: {str(e)}")
        return None

def main():
    lista_viajes = ListaViajes()
    
    while True:
        opcion = mostrar_menu()
        
        try:
            if opcion == "1":
                viaje = ingresar_viaje()
                if viaje:
                    lista_viajes.adicionar_viaje(viaje)
                    print("¡Viaje agregado exitosamente!")
                    
            elif opcion == "2":
                print("\n--- Lista de Viajes ---")
                lista_viajes.listar_viajes()
                
            elif opcion == "3":
                total = lista_viajes.calcular_total_precios()
                print(f"\nTotal de precios: ${total:.2f}")
                
            elif opcion == "4":
                promedio = lista_viajes.calcular_promedio_precios()
                print(f"\nPromedio de precios: ${promedio:.2f}")
                
            elif opcion == "5":
                viaje = lista_viajes.obtener_viaje_mas_costoso()
                if viaje:
                    print("\nViaje más costoso:")
                    print(viaje.obtener_info())
                else:
                    print("\nNo hay viajes registrados")
                    
            elif opcion == "6":
                print("\n¡Gracias por usar el sistema!")
                break
                
            else:
                print("\nOpción no válida. Por favor intente nuevamente.")
                
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except Exception as e:
            print(f"\nError inesperado: {str(e)}")
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main() 
