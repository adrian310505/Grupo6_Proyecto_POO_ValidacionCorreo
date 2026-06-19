# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# huesped.py
# Clase adicional 1 — Representa a un huésped registrado en el hotel.
# No hereda de ServicioHotel; es una entidad independiente del sistema.
# ─────────────────────────────────────────────────────────────────


class Huesped:
    """
    Clase que modela a un huésped del hotel.
    Aplica encapsulamiento en todos sus atributos mediante @property
    y @setter con validaciones para evitar datos incorrectos.
    """

    def __init__(self, id_huesped, nombre, telefono, email):
        """
        Constructor de Huesped.
        Todos los atributos pasan por sus respectivos setters al asignarse,
        activando las validaciones desde el momento de creación.

        Parámetros:
            id_huesped (str) : Identificador único del huésped.
            nombre     (str) : Nombre completo del huésped.
            telefono   (str) : Número de contacto del huésped.
            email      (str) : Correo electrónico válido del huésped.
        """
        self.id_huesped = id_huesped   # llama al @setter con validación
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    # ── Encapsulamiento: atributo _id_huesped ─────────────────────

    @property
    def id_huesped(self):
        """Getter: devuelve el ID del huésped."""
        return self._id_huesped

    @id_huesped.setter
    def id_huesped(self, valor):
        """Setter con validación: el ID no puede estar vacío."""
        if not valor or str(valor).strip() == "":
            raise ValueError("El ID del huésped no puede estar vacío.")
        self._id_huesped = str(valor).strip()

    # ── Encapsulamiento: atributo _nombre ─────────────────────────

    @property
    def nombre(self):
        """Getter: devuelve el nombre del huésped."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """
        Setter con validación: el nombre no puede estar vacío.
        Se aplica .title() para capitalizar correctamente cada palabra.
        """
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del huésped no puede estar vacío.")
        self._nombre = valor.strip().title()

    # ── Encapsulamiento: atributo _telefono ───────────────────────

    @property
    def telefono(self):
        """Getter: devuelve el teléfono del huésped."""
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        """Setter con validación: el teléfono no puede estar vacío."""
        if not valor or str(valor).strip() == "":
            raise ValueError("El teléfono no puede estar vacío.")
        self._telefono = str(valor).strip()

    # ── Encapsulamiento: atributo _email ──────────────────────────

    @property
    def email(self):
        """Getter: devuelve el email del huésped."""
        return self._email

    @email.setter
    def email(self, valor):
        """
        Setter con validación: el email debe contener el símbolo '@'
        para considerarse un correo electrónico válido.
        """
        if not valor or "@" not in valor:
            raise ValueError("El email ingresado no es válido.")
        self._email = valor.strip().lower()

    # ── Representación en cadena de texto ─────────────────────────

    def __str__(self):
        """
        Método especial __str__: devuelve la información del huésped
        en formato legible al usar print() sobre la instancia.
        """
        return (
            f"Huésped [{self._id_huesped}] "
            f"{self._nombre} | Tel: {self._telefono} | Email: {self._email}"
        )
