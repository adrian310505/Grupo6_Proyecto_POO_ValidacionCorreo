# Integrantes:
# - Luna Henry
# - Sánchez Adrian
# - Merchán Evelyn
# - Veintimilla Alejandra
# - Rodríguez Nayeli

# ─────────────────────────────────────────────────────────────────
# servicio/ServicioHotel.py
# Clase controladora: hereda de QMainWindow y conecta la interfaz
# gráfica con la lógica del dominio.
# Incluye validación de correo electrónico con expresiones regulares.
# ─────────────────────────────────────────────────────────────────

import re  # módulo para expresiones regulares

from PySide6.QtWidgets import QMainWindow, QMessageBox

from Gui.vtn_principal import Ui_ServicioHotel
from dominio.servicio_hotel import ServicioHotel as ServicioHotelDominio

# Expresión regular para validar correo electrónico
# Formato: algo@algo.algo (ej: usuario@gmail.com)
PATRON_CORREO = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'


class ServicioHotel(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ServicioHotel()
        self.ui.setupUi(self)

        self.setWindowTitle("Sistema de Gestión de Servicios de Hotel")
        self._servicios = []

        # Conectar botones con sus métodos
        self.ui.btn_guardar.clicked.connect(self.guardar_servicio)
        self.ui.btn_mostrar.clicked.connect(self.mostrar_servicios)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)

    def validar_campos(self, codigo, descripcion, precio_texto, correo):
        """
        Valida los 4 campos del formulario antes de crear el objeto.
        - Código: obligatorio, máximo 5 caracteres (limitado también en la UI)
        - Descripción: obligatorio, mínimo 5 caracteres
        - Precio base: obligatorio, número mayor a cero
        - Correo: obligatorio, formato válido con expresión regular
        """

        # ── Validación: Codigo ─────────────────────────────────────
        if codigo.strip() == "":
            raise ValueError("El campo CÓDIGO no puede estar vacío.")

        # ── Validación: Descripcion ────────────────────────────────
        if descripcion.strip() == "":
            raise ValueError("El campo DESCRIPCIÓN no puede estar vacío.")
        if len(descripcion.strip()) < 5:
            raise ValueError("La DESCRIPCIÓN debe tener al menos 5 caracteres.")

        # ── Validación: Precio base ────────────────────────────────
        if precio_texto.strip() == "":
            raise ValueError("El campo PRECIO BASE no puede estar vacío.")
        try:
            precio = float(precio_texto)
        except ValueError:
            raise ValueError("El PRECIO BASE debe ser un número válido (ej: 85.50).")
        if precio <= 0:
            raise ValueError("El PRECIO BASE debe ser mayor a cero.")
        if precio > 99999:
            raise ValueError("El PRECIO BASE no puede superar 99,999.")

        # ── Validación: Correo electrónico con regex ───────────────
        if correo.strip() == "":
            raise ValueError("El campo CORREO no puede estar vacío.")
        if not re.match(PATRON_CORREO, correo.strip()):
            raise ValueError(
                "El CORREO ingresado no tiene un formato válido.\n\n"
                "Ejemplos válidos:\n"
                "  • usuario@gmail.com\n"
                "  • nombre.apellido@hotmail.com\n"
                "  • estudiante2026@instituto.edu.ec"
            )

        return precio   # devuelve el precio ya convertido a float

    def guardar_servicio(self):
        """Lee el formulario, valida los 4 campos y guarda el servicio."""
        codigo      = self.ui.txt_Codigo.text()
        descripcion = self.ui.txt_descripcion.text()
        precio_txt  = self.ui.txt_precio_base.text()
        correo      = self.ui.txt_correo.text()

        try:
            # Validar todos los campos (incluyendo correo con regex)
            precio = self.validar_campos(codigo, descripcion, precio_txt, correo)

            # Crear objeto del dominio — los @setter también validan
            servicio = ServicioHotelDominio(
                codigo.strip(), descripcion.strip(), precio
            )
            self._servicios.append(servicio)

            # Mensaje de éxito incluyendo el correo validado
            QMessageBox.information(
                self,
                "✔ Registro exitoso",
                f"Servicio guardado correctamente:\n\n"
                f"  Código      : {servicio.codigo}\n"
                f"  Descripción : {servicio.descripcion}\n"
                f"  Precio base : ${servicio.precio_base:.2f}\n"
                f"  Correo      : {correo.strip()}"
            )
            self.limpiar_campos()

        except ValueError as e:
            # Mensaje de error con el problema específico
            QMessageBox.critical(self, "✘ Error de validación", str(e))

    def mostrar_servicios(self):
        """Muestra todos los servicios guardados."""
        if not self._servicios:
            QMessageBox.warning(
                self, "Sin registros", "No hay servicios guardados aún."
            )
            return

        texto = ""
        for i, sv in enumerate(self._servicios, 1):
            texto += (
                f"{i}. Código: {sv.codigo}  |  "
                f"Descripción: {sv.descripcion}  |  "
                f"Precio: ${sv.precio_base:.2f}\n"
            )

        QMessageBox.information(self, "Servicios registrados", texto)

    def limpiar_campos(self):
        """Limpia los 4 campos del formulario."""
        self.ui.txt_Codigo.clear()
        self.ui.txt_descripcion.clear()
        self.ui.txt_precio_base.clear()
        self.ui.txt_correo.clear()
        self.ui.txt_Codigo.setFocus()
