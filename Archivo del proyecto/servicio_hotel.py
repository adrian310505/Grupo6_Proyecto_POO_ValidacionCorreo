# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# servicio_hotel.py
# Superclase base del sistema de gestión de servicios del hotel.
# Toda reserva o servicio adicional hereda de esta clase.
# ─────────────────────────────────────────────────────────────────


class ServicioHotel:
    """
    Superclase que representa cualquier servicio ofrecido por el hotel.
    Define los atributos comunes y los métodos polimórficos que deben
    implementar todas las clases hijas (calcular_costo y mostrar_info).
    """

    def __init__(self, codigo, descripcion, precio_base):
        """
        Constructor de ServicioHotel.
        Inicializa los tres atributos comunes a todo servicio.
        Se usan los setters para que las validaciones se ejecuten
        desde el momento de la creación del objeto.

        Parámetros:
            codigo      (str)   : Identificador único del servicio.
            descripcion (str)   : Descripción breve del servicio.
            precio_base (float) : Precio base (por noche o por unidad).
        """
        self.codigo = codigo          # llama al @setter para validar
        self.descripcion = descripcion
        self.precio_base = precio_base

    # ── Encapsulamiento: atributo _codigo ──────────────────────────

    @property
    def codigo(self):
        """Getter: devuelve el código del servicio."""
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        """
        Setter con validación: el código no puede ser vacío ni solo espacios.
        Se almacena en mayúsculas para uniformidad.
        """
        if not valor or valor.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        self._codigo = valor.strip().upper()

    # ── Encapsulamiento: atributo _descripcion ─────────────────────

    @property
    def descripcion(self):
        """Getter: devuelve la descripción del servicio."""
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        """Setter con validación: la descripción no puede estar vacía."""
        if not valor or valor.strip() == "":
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = valor.strip()

    # ── Encapsulamiento: atributo _precio_base ─────────────────────

    @property
    def precio_base(self):
        """Getter: devuelve el precio base del servicio."""
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        """Setter con validación: el precio no puede ser negativo."""
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = valor

    # ── Métodos polimórficos (deben ser sobreescritos) ─────────────

    def calcular_costo(self):
        """
        Método polimórfico 1.
        Cada clase hija lo implementa con su propia lógica de costo.
        Si se llama directamente en la superclase lanza un error.
        """
        raise NotImplementedError("Subclases deben implementar calcular_costo().")

    def mostrar_info(self):
        """
        Método polimórfico 2.
        Cada clase hija lo implementa mostrando su propia información.
        Si se llama directamente en la superclase lanza un error.
        """
        raise NotImplementedError("Subclases deben implementar mostrar_info().")

    # ── Representación en cadena de texto ─────────────────────────

    def __str__(self):
        """
        Método especial __str__: permite imprimir el objeto directamente
        con print() y obtener una representación legible en consola.
        Llama a calcular_costo() de forma polimórfica.
        """
        return (f"[{self._codigo}] {self._descripcion} "
                f"| Precio base: ${self._precio_base:.2f} "
                f"| Costo total: ${self.calcular_costo():.2f}")
