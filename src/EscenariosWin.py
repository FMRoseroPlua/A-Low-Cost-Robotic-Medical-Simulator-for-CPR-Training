# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\EscenariosWin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EscenariosWin(object):
    def setupUi(self, EscenariosWin):
        EscenariosWin.setObjectName(_fromUtf8("EscenariosWin"))
        EscenariosWin.resize(677, 584)
        EscenariosWin.setMinimumSize(QtCore.QSize(677, 584))
        EscenariosWin.setMaximumSize(QtCore.QSize(840, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EscenariosWin.setWindowIcon(icon)
        EscenariosWin.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 50, 48, 255), stop:1 rgba(97, 91, 88, 255));\n"
""))
        self.btninstrucciones = QtGui.QPushButton(EscenariosWin)
        self.btninstrucciones.setGeometry(QtCore.QRect(500, 460, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninstrucciones.setFont(font)
        self.btninstrucciones.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/Instrucciones.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninstrucciones.setIcon(icon1)
        self.btninstrucciones.setIconSize(QtCore.QSize(40, 40))
        self.btninstrucciones.setObjectName(_fromUtf8("btninstrucciones"))
        self.btninicio = QtGui.QPushButton(EscenariosWin)
        self.btninicio.setEnabled(False)
        self.btninicio.setGeometry(QtCore.QRect(500, 320, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btninicio.setFont(font)
        self.btninicio.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/FIRST AID.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btninicio.setIcon(icon2)
        self.btninicio.setIconSize(QtCore.QSize(40, 40))
        self.btninicio.setObjectName(_fromUtf8("btninicio"))
        self.btnmenu = QtGui.QPushButton(EscenariosWin)
        self.btnmenu.setGeometry(QtCore.QRect(500, 520, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnmenu.setFont(font)
        self.btnmenu.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(194, 251, 21);\n"
"border: 1px solid;\n"
"border-radius:10px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/BRIGHTS HOME.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnmenu.setIcon(icon3)
        self.btnmenu.setIconSize(QtCore.QSize(40, 40))
        self.btnmenu.setObjectName(_fromUtf8("btnmenu"))
        self.Tabla = QtGui.QTableWidget(EscenariosWin)
        self.Tabla.setGeometry(QtCore.QRect(20, 300, 441, 271))
        self.Tabla.setStyleSheet(_fromUtf8("background-color: rgb(220, 220, 253);"))
        self.Tabla.setLineWidth(1)
        self.Tabla.setMidLineWidth(0)
        self.Tabla.setObjectName(_fromUtf8("Tabla"))
        self.Tabla.setColumnCount(4)
        self.Tabla.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.Tabla.setHorizontalHeaderItem(3, item)
        self.groupBox = QtGui.QGroupBox(EscenariosWin)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 641, 271))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setToolTip(_fromUtf8(""))
        self.groupBox.setWhatsThis(_fromUtf8(""))
        self.groupBox.setStyleSheet(_fromUtf8("color:rgb(170, 0, 127);\n"
"\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border:3px solid;\n"
"border-radius: 5px"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnanadir = QtGui.QPushButton(self.groupBox)
        self.btnanadir.setGeometry(QtCore.QRect(530, 56, 91, 27))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnanadir.setFont(font)
        self.btnanadir.setStyleSheet(_fromUtf8("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color:rgb(255, 85, 0);\n"
"    background-color: rgb(0, 255, 127);\n"
"    background-color: rgb(157, 247, 255);\n"
"    background-color: rgb(255, 255, 127);\n"
"    background-color: rgb(213, 155, 53);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnanadir.setObjectName(_fromUtf8("btnanadir"))
        self.cbtiempo = QtGui.QComboBox(self.groupBox)
        self.cbtiempo.setGeometry(QtCore.QRect(220, 60, 51, 22))
        self.cbtiempo.setStyleSheet(_fromUtf8("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 170);\n"
"border: 1px solid;\n"
"border-radius: 0px;"))
        self.cbtiempo.setObjectName(_fromUtf8("cbtiempo"))
        self.cbtiempo.addItem(_fromUtf8(""))
        self.cbtiempo.addItem(_fromUtf8(""))
        self.cbtiempo.addItem(_fromUtf8(""))
        self.cbtiempo.addItem(_fromUtf8(""))
        self.cbtiempo.addItem(_fromUtf8(""))
        self.cbtiempo.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 51, 21))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(255, 85, 0);\n"
"background-color: transparent;\n"
"border: 1px;\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cbpatologias = QtGui.QComboBox(self.groupBox)
        self.cbpatologias.setGeometry(QtCore.QRect(40, 60, 151, 22))
        self.cbpatologias.setStyleSheet(_fromUtf8("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 170);\n"
"border: 1px solid;\n"
"border-radius: 0px;"))
        self.cbpatologias.setObjectName(_fromUtf8("cbpatologias"))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.cbpatologias.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 30, 121, 21))
        self.label.setStyleSheet(_fromUtf8("color:rgb(255, 85, 0);\n"
"background-color: transparent;\n"
"border: 1px;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 30, 61, 16))
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(255, 85, 0);\n"
"background-color: transparent;\n"
"border: 1px;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(440, 40, 71, 16))
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(255, 85, 0);\n"
"background-color: transparent;\n"
"border: 1px;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.sbfrespiracion = QtGui.QSpinBox(self.groupBox)
        self.sbfrespiracion.setGeometry(QtCore.QRect(440, 60, 61, 22))
        self.sbfrespiracion.setStyleSheet(_fromUtf8("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 170);\n"
"border: 1px solid;\n"
"border-radius: 0px;"))
        self.sbfrespiracion.setMinimum(20)
        self.sbfrespiracion.setMaximum(40)
        self.sbfrespiracion.setSingleStep(1)
        self.sbfrespiracion.setObjectName(_fromUtf8("sbfrespiracion"))
        self.cbrespiracion = QtGui.QComboBox(self.groupBox)
        self.cbrespiracion.setGeometry(QtCore.QRect(300, 60, 111, 22))
        self.cbrespiracion.setStyleSheet(_fromUtf8("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 170);\n"
"border: 1px solid;\n"
"border-radius: 0px;"))
        self.cbrespiracion.setObjectName(_fromUtf8("cbrespiracion"))
        self.cbrespiracion.addItem(_fromUtf8(""))
        self.cbrespiracion.addItem(_fromUtf8(""))
        self.cbrespiracion.addItem(_fromUtf8(""))
        self.cbrespiracion.addItem(_fromUtf8(""))
        self.cbrespiracion.addItem(_fromUtf8(""))
        self.cbrespiracion.addItem(_fromUtf8(""))
        self.btncargar = QtGui.QPushButton(self.groupBox)
        self.btncargar.setGeometry(QtCore.QRect(530, 182, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btncargar.setFont(font)
        self.btncargar.setStyleSheet(_fromUtf8("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(130, 191, 186);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/open.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btncargar.setIcon(icon4)
        self.btncargar.setObjectName(_fromUtf8("btncargar"))
        self.btnguardar = QtGui.QPushButton(self.groupBox)
        self.btnguardar.setGeometry(QtCore.QRect(530, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnguardar.setFont(font)
        self.btnguardar.setStyleSheet(_fromUtf8("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(130, 191, 186);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/Save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnguardar.setIcon(icon5)
        self.btnguardar.setObjectName(_fromUtf8("btnguardar"))
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(20, 210, 361, 41))
        self.frame.setStyleSheet(_fromUtf8("color:rgb(170, 0, 127);\n"
"background-color: rgb(255, 170, 255);\n"
"border:1px solid;\n"
"border-color:rgb(0, 0, 0);\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btncambiar = QtGui.QPushButton(self.frame)
        self.btncambiar.setGeometry(QtCore.QRect(190, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btncambiar.setFont(font)
        self.btncambiar.setStyleSheet(_fromUtf8("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(130, 191, 186);\n"
"\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btncambiar.setObjectName(_fromUtf8("btncambiar"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 11, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("background-color: transparent;\n"
"border: 1px;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.sbmodificar = QtGui.QSpinBox(self.frame)
        self.sbmodificar.setGeometry(QtCore.QRect(100, 10, 61, 22))
        self.sbmodificar.setStyleSheet(_fromUtf8("color:rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 170);\n"
"border: 1px solid;\n"
"border-radius: 0px;"))
        self.sbmodificar.setMinimum(1)
        self.sbmodificar.setMaximum(1)
        self.sbmodificar.setObjectName(_fromUtf8("sbmodificar"))
        self.btnremover = QtGui.QPushButton(self.frame)
        self.btnremover.setGeometry(QtCore.QRect(270, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnremover.setFont(font)
        self.btnremover.setStyleSheet(_fromUtf8("QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(130, 191, 186);\n"
"border: 1px solid;\n"
"border-radius:5px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(241, 214, 0);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnremover.setObjectName(_fromUtf8("btnremover"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(440, 20, 81, 21))
        self.label_6.setStyleSheet(_fromUtf8("color:rgb(255, 85, 0);\n"
"background-color: transparent;\n"
"border: 1px;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(EscenariosWin)
        QtCore.QMetaObject.connectSlotsByName(EscenariosWin)

    def retranslateUi(self, EscenariosWin):
        EscenariosWin.setWindowTitle(_translate("EscenariosWin", "Simulador de RCP", None))
        self.btninstrucciones.setText(_translate("EscenariosWin", "Instrucciones", None))
        self.btninicio.setText(_translate("EscenariosWin", "Inicio", None))
        self.btnmenu.setText(_translate("EscenariosWin", "Menú", None))
        item = self.Tabla.horizontalHeaderItem(0)
        item.setText(_translate("EscenariosWin", "Ritmo Cardiaco", None))
        item = self.Tabla.horizontalHeaderItem(1)
        item.setText(_translate("EscenariosWin", "Duración", None))
        item = self.Tabla.horizontalHeaderItem(2)
        item.setText(_translate("EscenariosWin", "Respiración", None))
        item = self.Tabla.horizontalHeaderItem(3)
        item.setText(_translate("EscenariosWin", "F. Respiratoria", None))
        self.groupBox.setTitle(_translate("EscenariosWin", "Opciones", None))
        self.btnanadir.setText(_translate("EscenariosWin", "Añadir", None))
        self.cbtiempo.setItemText(0, _translate("EscenariosWin", "10 s", None))
        self.cbtiempo.setItemText(1, _translate("EscenariosWin", "20 s", None))
        self.cbtiempo.setItemText(2, _translate("EscenariosWin", "30 s", None))
        self.cbtiempo.setItemText(3, _translate("EscenariosWin", "40 s", None))
        self.cbtiempo.setItemText(4, _translate("EscenariosWin", "50 s", None))
        self.cbtiempo.setItemText(5, _translate("EscenariosWin", "60 s", None))
        self.label_2.setText(_translate("EscenariosWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Tiempo</span></p></body></html>", None))
        self.cbpatologias.setItemText(0, _translate("EscenariosWin", "Ritmo Sinusal", None))
        self.cbpatologias.setItemText(1, _translate("EscenariosWin", "Asistolia", None))
        self.cbpatologias.setItemText(2, _translate("EscenariosWin", "Bradicardia Sinusal", None))
        self.cbpatologias.setItemText(3, _translate("EscenariosWin", "Fibrilación Auricular", None))
        self.cbpatologias.setItemText(4, _translate("EscenariosWin", "Fibrilación Ventricular", None))
        self.cbpatologias.setItemText(5, _translate("EscenariosWin", "Taquicardia Ventricular", None))
        self.cbpatologias.setItemText(6, _translate("EscenariosWin", "Taquicardia Supraventricular", None))
        self.label.setText(_translate("EscenariosWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ritmos Cardiacos</span></p></body></html>", None))
        self.label_3.setText(_translate("EscenariosWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sonidos</span></p></body></html>", None))
        self.label_4.setText(_translate("EscenariosWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Frecuencia</span></p></body></html>", None))
        self.cbrespiracion.setItemText(0, _translate("EscenariosWin", "Ninguno", None))
        self.cbrespiracion.setItemText(1, _translate("EscenariosWin", "Jadeo", None))
        self.cbrespiracion.setItemText(2, _translate("EscenariosWin", "Respiración normal", None))
        self.cbrespiracion.setItemText(3, _translate("EscenariosWin", "Respiración agónica", None))
        self.cbrespiracion.setItemText(4, _translate("EscenariosWin", "Tos", None))
        self.cbrespiracion.setItemText(5, _translate("EscenariosWin", "Usuario", None))
        self.btncargar.setText(_translate("EscenariosWin", "Abrir", None))
        self.btnguardar.setText(_translate("EscenariosWin", "Guardar", None))
        self.btncambiar.setText(_translate("EscenariosWin", "Cambiar", None))
        self.label_5.setText(_translate("EscenariosWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Modificar</span></p></body></html>", None))
        self.btnremover.setText(_translate("EscenariosWin", "Eliminar", None))
        self.label_6.setText(_translate("EscenariosWin", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Respiratoria</span></p></body></html>", None))

import Iconos

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EscenariosWin = QtGui.QDialog()
    ui = Ui_EscenariosWin()
    ui.setupUi(EscenariosWin)
    EscenariosWin.show()
    sys.exit(app.exec_())

