import sys

from PySide6.QtWidgets import QApplication

from Gui import vtn_principal
from servicio.ServicioHotel import ServicioHotel

app = QApplication()
vtn_principal = ServicioHotel()
vtn_principal.show()
sys.exit(app.exec())

