# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# reserva_habitacion.py
# Clase hija 1 — Hereda de ServicioHotel.
# Modela la reserva de una habitación del hotel, calculando el costo
# por número de noches y aplicando descuento por larga estadía.
# ─────────────────────────────────────────────────────────────────

from servicio_hotel import ServicioHotel

# Constantes de negocio (UPPER_CASE según PEP8)
DESCUENTO_LARGA_ESTADIA = 0.10   # 10 % de descuento si la estadía es >= 7 noches
NOCHES_MINIMAS_DESCUENTO = 7    # Umbral para aplicar el descuento


class ReservaHabitacion(ServicioHotel):
    """
    Clase hija que representa la reserva de una habitación.
    Hereda atributos comunes (codigo, descripcion, precio_base) de ServicioHotel
    y agrega atributos propios: numero_noches y tipo_habitacion.

    Regla de negocio:
        costo = numero_noches × precio_por_noche
        Si numero_noches >= 7  →  se aplica 10% de descuento automáticamente.
    """

    # Tipos de habitación permitidos (constante de clase)
    TIPOS_VALIDOS = ("simple", "doble", "suite")

    def __init__(self, codigo, descripcion, precio_por_noche,
                 numero_noches, tipo_habitacion):
        """
        Constructor de ReservaHabitacion.
        Llama al constructor de la superclase con super() para heredar
        la inicialización de codigo, descripcion y precio_base.

        Parámetros:
            codigo           (str)   : Código único de la reserva.
            descripcion      (str)   : Descripción de la reserva.
            precio_por_noche (float) : Precio por cada noche de estadía.
            numero_noches    (int)   : Cantidad de noches reservadas.
            tipo_habitacion  (str)   : Tipo: 'simple', 'doble' o 'suite'.
        """
        super().__init__(codigo, descripcion, precio_por_noche)  # herencia
        self.numero_noches = numero_noches    # llama al @setter con validación
        self.tipo_habitacion = tipo_habitacion

    # ── Encapsulamiento: atributo _numero_noches ───────────────────

    @property
    def numero_noches(self):
        """Getter: devuelve el número de noches de la reserva."""
        return self._numero_noches

    @numero_noches.setter
    def numero_noches(self, valor):
        """
        Setter con validación: las noches deben ser mayor a cero.
        Se convierte a int() para garantizar que sea un número entero.
        """
        if valor <= 0:
            raise ValueError("El número de noches debe ser mayor a cero.")
        self._numero_noches = int(valor)   # conversión explícita a entero

    # ── Encapsulamiento: atributo _tipo_habitacion ─────────────────

    @property
    def tipo_habitacion(self):
        """Getter: devuelve el tipo de habitación."""
        return self._tipo_habitacion

    @tipo_habitacion.setter
    def tipo_habitacion(self, valor):
        """
        Setter con validación: solo se aceptan tipos definidos en TIPOS_VALIDOS.
        Se convierte a minúsculas para comparación uniforme.
        """
        if valor.lower() not in self.TIPOS_VALIDOS:
            raise ValueError(
                f"Tipo de habitación inválido. Opciones: {self.TIPOS_VALIDOS}"
            )
        self._tipo_habitacion = valor.lower()

    # ── Método polimórfico 1: calcular_costo ──────────────────────

    def calcular_costo(self):
        """
        Sobreescribe calcular_costo() de la superclase.
        Aplica la regla de negocio: noches × precio_por_noche.
        Si la estadía alcanza el umbral, se descuenta el 10%.
        """
        subtotal = self._numero_noches * self._precio_base
        if self._numero_noches >= NOCHES_MINIMAS_DESCUENTO:
            subtotal *= (1 - DESCUENTO_LARGA_ESTADIA)  # aplica descuento
        return subtotal

    # ── Método polimórfico 2: mostrar_info ───────────────────────

    def mostrar_info(self):
        """
        Sobreescribe mostrar_info() de la superclase.
        Devuelve un string con todos los detalles de la reserva,
        indicando si se aplicó o no el descuento por larga estadía.
        """
        descuento = (
            f"✔ Descuento {int(DESCUENTO_LARGA_ESTADIA * 100)}% aplicado"
            if self._numero_noches >= NOCHES_MINIMAS_DESCUENTO
            else "Sin descuento"
        )
        return (
            f"--- Reserva de Habitación ---\n"
            f"  Código        : {self._codigo}\n"
            f"  Descripción   : {self._descripcion}\n"
            f"  Tipo          : {self._tipo_habitacion.capitalize()}\n"
            f"  Precio/noche  : ${self._precio_base:.2f}\n"
            f"  Noches        : {self._numero_noches}\n"
            f"  {descuento}\n"
            f"  TOTAL         : ${self.calcular_costo():.2f}"
        )

    # ── Representación en cadena de texto ─────────────────────────

    def __str__(self):
        """
        Método especial __str__: representación compacta del objeto.
        Se muestra al usar print() directamente sobre la instancia.
        """
        return (
            f"ReservaHabitacion({self._codigo} | "
            f"{self._tipo_habitacion.capitalize()} | "
            f"{self._numero_noches} noche(s) | "
            f"Total: ${self.calcular_costo():.2f})"
        )
