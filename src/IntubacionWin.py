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
        self.label.setGeometry(QtCore.QRect(220, 20, 491, 511))
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/Imagenes/ViaR.jpg);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Intubacion)
        self.pushButton.setGeometry(QtCore.QRect(30, 520, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Intubacion)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 520, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(Intubacion)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(510, 430, 22, 22))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);\n"
"border-radius:11px;\n"
""))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Intubacion)
        self.label_3.setGeometry(QtCore.QRect(550, 440, 22, 22))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);\n"
"border-radius:11px;"))
        self.label_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Intubacion)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,0);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lbfrecuencia = QtGui.QLabel(Intubacion)
        self.lbfrecuencia.setEnabled(True)
        self.lbfrecuencia.setGeometry(QtCore.QRect(20, 290, 171, 31))
        self.lbfrecuencia.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167,0);\n"
"color:  rgb(241, 214, 0);\n"
"}\n"
"QLabel:hover{\n"
"background-color: rgb(255,255, 255);\n"
"color:rgb(0,0,0);\n"
" }"))
        self.lbfrecuencia.setObjectName(_fromUtf8("lbfrecuencia"))
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.lbfrecuencia.raise_()
        self.label.raise_()

        self.retranslateUi(Intubacion)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_3.raise_)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_2.lower)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_3.lower)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_2.raise_)
        QtCore.QMetaObject.connectSlotsByName(Intubacion)

    def retranslateUi(self, Intubacion):
        Intubacion.setWindowTitle(_translate("Intubacion", "Dialog", None))
        self.pushButton.setText(_translate("Intubacion", "Laringe", None))
        self.pushButton_2.setText(_translate("Intubacion", "Esofago", None))
        self.label_4.setText(_translate("Intubacion", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado:</span></p></body></html>", None))
        self.lbfrecuencia.setText(_translate("Intubacion", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Sin intubación</span></p></body></html>", None))

import Iconos

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Intubacion = QtGui.QDialog()
    ui = Ui_Intubacion()
    ui.setupUi(Intubacion)
    Intubacion.show()
    sys.exit(app.exec_())

