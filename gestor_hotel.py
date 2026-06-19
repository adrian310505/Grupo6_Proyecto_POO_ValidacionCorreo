# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# gestor_hotel.py
# Clase adicional 2 — Gestiona huéspedes y servicios del hotel.
# Contiene los dos métodos polimórficos obligatorios del sistema:
#   - calcular_costo()  →  recorre lista heterogénea y suma costos
#   - mostrar_info()    →  recorre lista heterogénea y muestra detalle
# ─────────────────────────────────────────────────────────────────

from servicio_hotel import ServicioHotel


class GestorHotel:
    """
    Clase gestora que coordina el funcionamiento del hotel.
    Almacena listas de huéspedes y servicios, y ejecuta operaciones
    sobre ellos de forma polimórfica (sin conocer el tipo concreto
    de cada objeto en la lista).
    """

    # Nombre por defecto del hotel (constante de clase en UPPER_CASE)
    NOMBRE_HOTEL = "HOTEL PARAÍSO"

    def __init__(self, nombre_hotel=None):
        """
        Constructor de GestorHotel.
        Inicializa las listas internas de servicios y huéspedes.
        Los atributos son privados (_) para mantener encapsulamiento.

        Parámetro:
            nombre_hotel (str): Nombre del hotel (opcional).
        """
        self._nombre_hotel = nombre_hotel or self.NOMBRE_HOTEL
        self._servicios: list[ServicioHotel] = []  # lista de la superclase
        self._huespedes = []                        # lista de objetos Huesped

    # ── Gestión de huéspedes ──────────────────────────────────────

    def registrar_huesped(self, huesped):
        """
        Agrega un objeto Huesped a la lista interna y confirma en consola.

        Parámetro:
            huesped (Huesped): Instancia del huésped a registrar.
        """
        self._huespedes.append(huesped)
        print(f"✔ Huésped registrado: {huesped.nombre}")

    def listar_huespedes(self):
        """Imprime en consola todos los huéspedes registrados."""
        if not self._huespedes:
            print("No hay huéspedes registrados.")
            return
        print(f"\n{'='*45}")
        print(f"  HUÉSPEDES — {self._nombre_hotel}")
        print(f"{'='*45}")
        for h in self._huespedes:
            print(f"  {h}")   # usa __str__() de la clase Huesped

    # ── Gestión de servicios ──────────────────────────────────────

    def agregar_servicio(self, servicio: ServicioHotel):
        """
        Agrega un objeto de tipo ServicioHotel (o cualquier subclase)
        a la lista interna y confirma en consola.

        Parámetro:
            servicio (ServicioHotel): Instancia del servicio a agregar.
        """
        self._servicios.append(servicio)
        print(f"✔ Servicio agregado: {servicio.codigo}")

    # ── Método polimórfico 1: calcular_costo ──────────────────────

    def calcular_costo(self, servicios=None):
        """
        Recorre la lista de servicios y llama a calcular_costo() en
        cada objeto SIN preguntar su tipo concreto (polimorfismo puro).
        Cada objeto sabe calcular su propio costo según su clase.

        Parámetro:
            servicios (list): Lista de objetos ServicioHotel a evaluar.
                              Si es None, usa la lista interna del gestor.

        Retorna:
            float: Suma total de costos de todos los servicios.
        """
        lista = servicios if servicios is not None else self._servicios
        total = 0.0
        print(f"\n{'='*45}")
        print("  CÁLCULO DE COSTOS")
        print(f"{'='*45}")
        for servicio in lista:
            costo = servicio.calcular_costo()   # llamada polimórfica
            print(f"  {servicio.codigo:<12} → ${costo:>10.2f}")
            total += costo
        print(f"{'─'*45}")
        print(f"  {'TOTAL':<12}    ${total:>10.2f}")
        print(f"{'='*45}")
        return total

    # ── Método polimórfico 2: mostrar_info ───────────────────────

    def mostrar_info(self, servicios=None):
        """
        Recorre la lista de servicios y llama a mostrar_info() en
        cada objeto SIN preguntar su tipo concreto (polimorfismo puro).
        Cada objeto sabe mostrar su propia información según su clase.

        Parámetro:
            servicios (list): Lista de objetos ServicioHotel a mostrar.
                              Si es None, usa la lista interna del gestor.
        """
        lista = servicios if servicios is not None else self._servicios
        print(f"\n{'='*45}")
        print(f"  REPORTE DE SERVICIOS — {self._nombre_hotel}")
        print(f"{'='*45}")
        for servicio in lista:
            print(servicio.mostrar_info())   # llamada polimórfica
            print(f"{'─'*45}")

    def generar_reporte_completo(self):
        """
        Método de conveniencia: ejecuta en secuencia el listado de
        huéspedes, el reporte de servicios y el cálculo de costos.
        Retorna el total facturado.
        """
        self.listar_huespedes()
        self.mostrar_info()
        total = self.calcular_costo()
        return total
