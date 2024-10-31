from clases import NodoViaje

class ListaViajes:
    def __init__(self):
        """
        Inicializa una lista vacía de viajes
        """
        self.head = None
        self.cantidad_elementos = 0

    def adicionar_viaje(self, viaje):
        """
        Adiciona un viaje a la lista con validaciones
        Args:
            viaje: Objeto de la clase Viaje a adicionar
        Raises:
            ValueError: Si algún campo no cumple con las validaciones
        """
        # Validar que el viaje no sea None
        if viaje is None:
            raise ValueError("El viaje no puede ser None")

        # Validar campos obligatorios
        if not viaje.origen or not isinstance(viaje.origen, str) or viaje.origen.strip() == "":
            raise ValueError("El origen es obligatorio y debe ser texto")
            
        if not viaje.destino or not isinstance(viaje.destino, str) or viaje.destino.strip() == "":
            raise ValueError("El destino es obligatorio y debe ser texto")
            
        if not viaje.fecha or not isinstance(viaje.fecha, str) or viaje.fecha.strip() == "":
            raise ValueError("La fecha es obligatoria y debe ser texto")

        # Validar que el precio sea numérico y positivo
        if not isinstance(viaje.precio, (int, float)):
            raise ValueError("El precio debe ser un valor numérico")
            
        if viaje.precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")

        # Validar formato de fecha (asumiendo formato YYYY-MM-DD)
        try:
            from datetime import datetime
            datetime.strptime(viaje.fecha, '%Y-%m-%d')
        except ValueError:
            raise ValueError("La fecha debe tener el formato YYYY-MM-DD")

        # Si todas las validaciones pasan, crear el nuevo nodo
        nodo_nuevo = NodoViaje(viaje)

        # Escenario 1: Lista vacía
        if self.head is None:
            self.head = nodo_nuevo
            self.cantidad_elementos = 1
        # Escenario 2: Lista no vacía
        else:
            actual = self.head
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo_nuevo
            self.cantidad_elementos += 1
    
    def listar_viajes(self):
        """
        Muestra todos los viajes en la lista
        """
        actual = self.head
        if actual is None:
            print("No hay viajes registrados")
            return
        
        while actual is not None:
            print(actual.viaje.obtener_info())
            actual = actual.siguiente 

    def calcular_total_precios(self):
        """
        Calcula la suma total de los precios de todos los viajes
        Returns:
            float: Suma total de los precios
        """
        total = 0
        actual = self.head
        
        while actual is not None:
            total += actual.viaje.precio
            actual = actual.siguiente
            
        return total

    def calcular_promedio_precios(self):
        """
        Calcula el promedio de los precios de todos los viajes
        Returns:
            float: Promedio de los precios. Retorna 0 si la lista está vacía.
        """
        if self.cantidad_elementos == 0:
            return 0
            
        total = self.calcular_total_precios()
        return total / self.cantidad_elementos

    def obtener_viaje_mas_costoso(self):
        """
        Encuentra y retorna el viaje con el precio más alto
        Returns:
            Viaje: Objeto viaje más costoso. None si la lista está vacía.
        """
        if self.head is None:
            return None
            
        actual = self.head
        viaje_mas_costoso = actual.viaje
        
        while actual is not None:
            if actual.viaje.precio > viaje_mas_costoso.precio:
                viaje_mas_costoso = actual.viaje
            actual = actual.siguiente
            
        return viaje_mas_costoso
