# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\IntubacionWin.ui'
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

class Ui_Intubacion(object):
    def setupUi(self, Intubacion):
        Intubacion.setObjectName(_fromUtf8("Intubacion"))
        Intubacion.resize(720, 560)
        Intubacion.setMinimumSize(QtCore.QSize(720, 560))
        Intubacion.setMaximumSize(QtCore.QSize(720, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Intubacion.setWindowIcon(icon)
        Intubacion.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 50, 48, 255), stop:1 rgba(97, 91, 88, 255));\n"
""))
        self.label = QtGui.QLabel(Intubacion)
        self.label.setGeometry(QtCore.QRect(250, 30, 401, 511))
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/Imagenes/Endof.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Intubacion)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(532, 320, 22, 22))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);\n"
"border-radius:11px;\n"
""))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Intubacion)
        self.label_3.setGeometry(QtCore.QRect(582, 310, 22, 22))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"border-radius:11px;"))
        self.label_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Intubacion)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lbfrecuencia = QtGui.QLabel(Intubacion)
        self.lbfrecuencia.setEnabled(True)
        self.lbfrecuencia.setGeometry(QtCore.QRect(20, 330, 171, 31))
        self.lbfrecuencia.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167,0);\n"
"color:  rgb(241, 214, 0);\n"
"}\n"
"QLabel:hover{\n"
"background-color: rgb(255,255, 255);\n"
"color:rgb(0,0,0);\n"
" }"))
        self.lbfrecuencia.setObjectName(_fromUtf8("lbfrecuencia"))
        self.label_5 = QtGui.QLabel(Intubacion)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,0);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.btnabrir = QtGui.QPushButton(Intubacion)
        self.btnabrir.setGeometry(QtCore.QRect(30, 160, 75, 23))
        self.btnabrir.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(255, 164, 16);\n"
"background-color: rgb(153, 230, 0);\n"
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
        self.btnabrir.setObjectName(_fromUtf8("btnabrir"))
        self.btncerrar = QtGui.QPushButton(Intubacion)
        self.btncerrar.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.btncerrar.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(153, 230, 0);\n"
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
        self.btncerrar.setObjectName(_fromUtf8("btncerrar"))
        self.lbboca = QtGui.QLabel(Intubacion)
        self.lbboca.setEnabled(True)
        self.lbboca.setGeometry(QtCore.QRect(20, 210, 171, 31))
        self.lbboca.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167,0);\n"
"color:  rgb(241, 214, 0);\n"
"}\n"
"QLabel:hover{\n"
"background-color: rgb(255,255, 255);\n"
"color:rgb(0,0,0);\n"
" }"))
        self.lbboca.setObjectName(_fromUtf8("lbboca"))
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lbfrecuencia.raise_()
        self.label_5.raise_()
        self.btnabrir.raise_()
        self.btncerrar.raise_()
        self.label.raise_()
        self.lbboca.raise_()

        self.retranslateUi(Intubacion)
        QtCore.QMetaObject.connectSlotsByName(Intubacion)

    def retranslateUi(self, Intubacion):
        Intubacion.setWindowTitle(_translate("Intubacion", "Dialog", None))
        self.label_4.setText(_translate("Intubacion", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.lbfrecuencia.setText(_translate("Intubacion", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Sin intubación</span></p></body></html>", None))
        self.label_5.setText(_translate("Intubacion", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Mandíbula:</span></p></body></html>", None))
        self.btnabrir.setText(_translate("Intubacion", "Abrir", None))
        self.btncerrar.setText(_translate("Intubacion", "Cerrar", None))
        self.lbboca.setText(_translate("Intubacion", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Boca abierta</span></p></body></html>", None))

import Iconos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Intubacion = QtGui.QDialog()
    ui = Ui_Intubacion()
    ui.setupUi(Intubacion)
    Intubacion.show()
    sys.exit(app.exec_())

