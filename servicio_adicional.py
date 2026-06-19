# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# servicio_adicional.py
# Clase hija 2 — Hereda de ServicioHotel.
# Modela servicios adicionales del hotel (spa, lavandería, etc.),
# calculando el costo por cantidad consumida y recargo si es urgente.
# ─────────────────────────────────────────────────────────────────

from servicio_hotel import ServicioHotel

# Constante de negocio: recargo por urgencia (UPPER_CASE según PEP8)
RECARGO_URGENTE = 0.20   # 20 % extra si el servicio es marcado como urgente


class ServicioAdicional(ServicioHotel):
    """
    Clase hija que representa un servicio adicional del hotel.
    Hereda de ServicioHotel y agrega: cantidad, tipo_servicio y urgente.

    Regla de negocio:
        costo = cantidad × precio_por_unidad
        Si urgente == True  →  se aplica un recargo del 20% sobre el subtotal.
    """

    # Tipos de servicio permitidos (constante de clase)
    TIPOS_VALIDOS = ("spa", "lavanderia", "room_service",
                     "transporte", "tours", "otro")

    def __init__(self, codigo, descripcion, precio_por_unidad,
                 cantidad, tipo_servicio, urgente=False):
        """
        Constructor de ServicioAdicional.
        Llama al constructor de la superclase con super() para heredar
        la inicialización de codigo, descripcion y precio_base.

        Parámetros:
            codigo            (str)   : Código único del servicio.
            descripcion       (str)   : Descripción del servicio.
            precio_por_unidad (float) : Precio por cada unidad del servicio.
            cantidad          (int/float): Cantidad consumida del servicio.
            tipo_servicio     (str)   : Categoría del servicio adicional.
            urgente           (bool)  : True si se requiere atención urgente.
        """
        super().__init__(codigo, descripcion, precio_por_unidad)  # herencia
        self.cantidad = cantidad          # llama al @setter con validación
        self.tipo_servicio = tipo_servicio
        self.urgente = urgente

    # ── Encapsulamiento: atributo _cantidad ────────────────────────

    @property
    def cantidad(self):
        """Getter: devuelve la cantidad del servicio consumida."""
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        """Setter con validación: la cantidad debe ser mayor a cero."""
        if valor <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        self._cantidad = valor

    # ── Encapsulamiento: atributo _tipo_servicio ───────────────────

    @property
    def tipo_servicio(self):
        """Getter: devuelve el tipo de servicio adicional."""
        return self._tipo_servicio

    @tipo_servicio.setter
    def tipo_servicio(self, valor):
        """
        Setter con validación: solo se aceptan tipos en TIPOS_VALIDOS.
        Se convierte a minúsculas para comparación uniforme.
        """
        if valor.lower() not in self.TIPOS_VALIDOS:
            raise ValueError(
                f"Tipo de servicio inválido. Opciones: {self.TIPOS_VALIDOS}"
            )
        self._tipo_servicio = valor.lower()

    # ── Encapsulamiento: atributo _urgente ─────────────────────────

    @property
    def urgente(self):
        """Getter: devuelve si el servicio es urgente (True/False)."""
        return self._urgente

    @urgente.setter
    def urgente(self, valor):
        """
        Setter con validación: el valor debe ser booleano (True o False).
        Previene que se asigne un string o número por error.
        """
        if not isinstance(valor, bool):
            raise ValueError("El campo 'urgente' debe ser True o False.")
        self._urgente = valor

    # ── Método polimórfico 1: calcular_costo ──────────────────────

    def calcular_costo(self):
        """
        Sobreescribe calcular_costo() de la superclase.
        Aplica la regla de negocio: cantidad × precio_por_unidad.
        Si el servicio es urgente, se añade el 20% de recargo.
        """
        subtotal = self._cantidad * self._precio_base
        if self._urgente:
            subtotal *= (1 + RECARGO_URGENTE)  # aplica recargo por urgencia
        return subtotal

    # ── Método polimórfico 2: mostrar_info ───────────────────────

    def mostrar_info(self):
        """
        Sobreescribe mostrar_info() de la superclase.
        Devuelve un string con todos los detalles del servicio adicional,
        indicando si se aplicó o no el recargo por urgencia.
        """
        urgencia = (
            f"⚠ Recargo urgente {int(RECARGO_URGENTE * 100)}% incluido"
            if self._urgente
            else "Servicio estándar"
        )
        return (
            f"--- Servicio Adicional ---\n"
            f"  Código        : {self._codigo}\n"
            f"  Descripción   : {self._descripcion}\n"
            f"  Tipo          : {self._tipo_servicio.replace('_', ' ').title()}\n"
            f"  Precio/unidad : ${self._precio_base:.2f}\n"
            f"  Cantidad      : {self._cantidad}\n"
            f"  {urgencia}\n"
            f"  TOTAL         : ${self.calcular_costo():.2f}"
        )

    # ── Representación en cadena de texto ─────────────────────────

    def __str__(self):
        """
        Método especial __str__: representación compacta del objeto.
        Se muestra al usar print() directamente sobre la instancia.
        """
        return (
            f"ServicioAdicional({self._codigo} | "
            f"{self._tipo_servicio.replace('_', ' ').title()} | "
            f"Cant: {self._cantidad} | "
            f"Total: ${self.calcular_costo():.2f})"
        )
