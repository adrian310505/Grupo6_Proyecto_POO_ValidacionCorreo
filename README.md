[README (3).md](https://github.com/user-attachments/files/29145480/README.3.md)
# Grupo6_Proyecto_POO_ValidacionCorreo# 🏨 Sistema de Gestión de Hotel

**Programación Orientada a Objetos con PySide6**

---

## 📋 Descripción del proyecto

Sistema de gestión de servicios hoteleros desarrollado en Python con interfaz gráfica PySide6. Aplica los cuatro pilares de la POO: encapsulamiento, herencia, polimorfismo y abstracción. La arquitectura separa la lógica de negocio (dominio) de la interfaz gráfica, conectadas mediante una clase controladora.

---

## 👥 Integrantes

- Luna Henry
- Sánchez Adrián
- Merchán Evelyn
- Veintimilla Alejandra
- Rodríguez Nayeli

---

## 📁 Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `servicio_hotel.py` | Clase base (superclase) — atributos comunes y métodos abstractos |
| `reserva_habitacion.py` | Clase hija 1 — reserva con descuento por larga estadía |
| `servicio_adicional.py` | Clase hija 2 — servicio con recargo por urgencia |
| `huesped.py` | Clase adicional — entidad independiente del huésped |
| `gestor_hotel.py` | Gestor — orquesta huéspedes y servicios, aplica polimorfismo |
| `ServicioHotel.py` | Controlador GUI — conecta interfaz con lógica del dominio |
| `vtn_principal.py` | UI generada por Qt Designer — ventana principal |
| `vtn_principal.ui` | Archivo fuente de la interfaz Qt (.ui) |

---

## 🏗️ Jerarquía de clases

### Clase base: `ServicioHotel`
Clase abstracta con los atributos comunes a todos los servicios: `codigo`, `descripcion` y `precio_base`. Declara los métodos abstractos `calcular_costo()` y `mostrar_info()` que cada subclase debe implementar.

### Clase hija 1: `ReservaHabitacion`
Hereda de `ServicioHotel`. Agrega `numero_noches` y `tipo_habitacion` (`simple`, `doble`, `suite`).

> **Regla de negocio:** `costo = noches × precio_por_noche`. Si la estadía es ≥ 7 noches → descuento automático del **10%**.

### Clase hija 2: `ServicioAdicional`
Hereda de `ServicioHotel`. Agrega `cantidad`, `tipo_servicio` y `urgente` (booleano).

> **Regla de negocio:** `costo = cantidad × precio_por_unidad`. Si `urgente = True` → recargo del **20%**.

### Clase adicional: `Huesped`
Entidad independiente (no hereda de `ServicioHotel`). Almacena `id_huesped`, `nombre`, `telefono` y `email` con encapsulamiento completo.

### Clase gestora: `GestorHotel`
Orquesta el sistema. Sus métodos `calcular_costo()` y `mostrar_info()` recorren listas heterogéneas sin preguntar el tipo concreto de cada objeto — **polimorfismo puro**.

---

## ✅ Validaciones implementadas

El sistema aplica validaciones en **dos niveles**:
- **Nivel GUI** (`ServicioHotel.py`): valida el formulario antes de crear cualquier objeto.
- **Nivel dominio** (`@setter`): cada clase valida sus propios atributos al asignarse.

| Campo | Regla de validación |
|---|---|
| Código | Obligatorio, máximo 5 caracteres (limitado también en la UI Qt) |
| Descripción | Obligatorio, mínimo 5 caracteres (tras aplicar `strip()`) |
| Precio base | Obligatorio, número decimal mayor a 0 y no superior a 99 999 |
| Correo | Obligatorio, validado con expresión regular (`re.match`) |
| Número de noches | Entero mayor a cero — `@setter` en `ReservaHabitacion`, conversión explícita a `int` |
| Tipo de habitación | Solo acepta: `simple`, `doble`, `suite` — comparación en minúsculas |
| Cantidad | Mayor a cero — `@setter` en `ServicioAdicional` |
| Tipo de servicio | Solo acepta: `spa`, `lavanderia`, `room_service`, `transporte`, `tours`, `otro` |
| Urgente | Debe ser booleano (`True`/`False`) — previene asignación de string o número |
| ID Huésped | No puede estar vacío — se convierte a `str` y se aplica `strip()` |
| Email Huésped | Debe contener `@` — validación básica en `@setter` de `Huesped` |

### Validación de correo con expresión regular

La validación del correo en `ServicioHotel.py` usa el módulo `re` con el siguiente patrón:

```python
PATRON_CORREO = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
```

Verifica la estructura `usuario@dominio.extension` y se aplica con `re.match()` antes de guardar el servicio. Ejemplos válidos:

```
usuario@gmail.com
nombre.apellido@hotmail.com
estudiante2026@instituto.edu.ec
```

### Manejo de errores

Todas las validaciones lanzan `ValueError` con mensajes descriptivos. La clase controladora los captura con `try/except` y los muestra mediante `QMessageBox.critical()`, evitando que la aplicación se cierre inesperadamente.

---

## 🛠️ Tecnologías

- **Python 3.x** — lenguaje principal
- **PySide6** — framework para la interfaz gráfica (Qt 6)
- **Qt Designer** — diseño visual de la ventana (`.ui`)
- **Módulo `re`** — expresiones regulares para validación de correo

---

## ▶️ Instrucciones de ejecución

**Requisito previo:**
```bash
pip install PySide6
```

**Ejecutar la aplicación:**
```bash
python ServicioHotel.py
```

**Botones disponibles en la ventana:**
- **Guardar** — valida los campos y registra el servicio
- **Mostrar** — lista todos los servicios guardados en la sesión
- **Limpiar** — borra todos los campos del formulario

---

*Proyecto académico — Programación Orientada a Objetos*
