# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_ServicioHotel(object):
    def setupUi(self, ServicioHotel):
        if not ServicioHotel.objectName():
            ServicioHotel.setObjectName(u"ServicioHotel")
        ServicioHotel.resize(1040, 697)
        self.centralwidget = QWidget(ServicioHotel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(180, 20, 600, 50))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setStyleSheet(u"color: #2c3e50;")
        self.lbl_Codigo = QLabel(self.centralwidget)
        self.lbl_Codigo.setObjectName(u"lbl_Codigo")
        self.lbl_Codigo.setGeometry(QRect(190, 100, 130, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.lbl_Codigo.setFont(font1)
        self.lbl_Codigo.setStyleSheet(u"background-color: #f0f0f0; color: #000000; border-radius: 5px;")
        self.txt_Codigo = QLineEdit(self.centralwidget)
        self.txt_Codigo.setObjectName(u"txt_Codigo")
        self.txt_Codigo.setGeometry(QRect(350, 100, 200, 41))
        self.txt_Codigo.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.txt_Codigo.setMaxLength(5)
        self.lbl_descripcion = QLabel(self.centralwidget)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")
        self.lbl_descripcion.setGeometry(QRect(190, 180, 130, 41))
        self.lbl_descripcion.setFont(font1)
        self.lbl_descripcion.setStyleSheet(u"background-color: #f0f0f0; color: #000000; border-radius: 5px;")
        self.txt_descripcion = QLineEdit(self.centralwidget)
        self.txt_descripcion.setObjectName(u"txt_descripcion")
        self.txt_descripcion.setGeometry(QRect(350, 180, 200, 41))
        self.txt_descripcion.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.lbl_precio_base = QLabel(self.centralwidget)
        self.lbl_precio_base.setObjectName(u"lbl_precio_base")
        self.lbl_precio_base.setGeometry(QRect(190, 260, 130, 41))
        self.lbl_precio_base.setFont(font1)
        self.lbl_precio_base.setStyleSheet(u"background-color: #f0f0f0; color: #000000; border-radius: 5px;")
        self.txt_precio_base = QLineEdit(self.centralwidget)
        self.txt_precio_base.setObjectName(u"txt_precio_base")
        self.txt_precio_base.setGeometry(QRect(350, 260, 200, 41))
        self.txt_precio_base.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.lbl_correo = QLabel(self.centralwidget)
        self.lbl_correo.setObjectName(u"lbl_correo")
        self.lbl_correo.setGeometry(QRect(190, 340, 130, 41))
        self.lbl_correo.setFont(font1)
        self.lbl_correo.setStyleSheet(u"background-color: #f0f0f0; color: #000000; border-radius: 5px;")
        self.txt_correo = QLineEdit(self.centralwidget)
        self.txt_correo.setObjectName(u"txt_correo")
        self.txt_correo.setGeometry(QRect(350, 340, 200, 41))
        self.txt_correo.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.btn_guardar = QPushButton(self.centralwidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(190, 430, 150, 45))
        self.btn_guardar.setStyleSheet(u"background-color: #27ae60; color: white; font-size: 14px; border-radius: 8px;")
        self.btn_mostrar = QPushButton(self.centralwidget)
        self.btn_mostrar.setObjectName(u"btn_mostrar")
        self.btn_mostrar.setGeometry(QRect(370, 430, 150, 45))
        self.btn_mostrar.setStyleSheet(u"background-color: #2980b9; color: white; font-size: 14px; border-radius: 8px;")
        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(550, 430, 150, 45))
        self.btn_limpiar.setStyleSheet(u"background-color: #e74c3c; color: white; font-size: 14px; border-radius: 8px;")
        ServicioHotel.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ServicioHotel)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1040, 26))
        ServicioHotel.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ServicioHotel)
        self.statusbar.setObjectName(u"statusbar")
        ServicioHotel.setStatusBar(self.statusbar)

        self.retranslateUi(ServicioHotel)

        QMetaObject.connectSlotsByName(ServicioHotel)
    # setupUi

    def retranslateUi(self, ServicioHotel):
        ServicioHotel.setWindowTitle(QCoreApplication.translate("ServicioHotel", u"Sistema de Gesti\u00f3n de Servicios de Hotel", None))
        self.lbl_titulo.setText(QCoreApplication.translate("ServicioHotel", u"\U0001f3e8 Sistema de Gesti\U000000f3n de Hotel", None))
        self.lbl_Codigo.setText(QCoreApplication.translate("ServicioHotel", u"Codigo:", None))
        self.lbl_descripcion.setText(QCoreApplication.translate("ServicioHotel", u"Descripcion:", None))
        self.lbl_precio_base.setText(QCoreApplication.translate("ServicioHotel", u"Precio_base:", None))
        self.lbl_correo.setText(QCoreApplication.translate("ServicioHotel", u"Correo:", None))
        self.btn_guardar.setText(QCoreApplication.translate("ServicioHotel", u"Guardar", None))
        self.btn_mostrar.setText(QCoreApplication.translate("ServicioHotel", u"Mostrar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("ServicioHotel", u"Limpiar", None))
    # retranslateUi

