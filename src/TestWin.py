# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\TestWin.ui'
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

class Ui_TestWin(object):
    def setupUi(self, TestWin):
        TestWin.setObjectName(_fromUtf8("TestWin"))
        TestWin.resize(460, 525)
        TestWin.setMinimumSize(QtCore.QSize(0, 0))
        TestWin.setMaximumSize(QtCore.QSize(460, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TestWin.setWindowIcon(icon)
        TestWin.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 50, 48, 255), stop:1 rgba(97, 91, 88, 255));\n"
""))
        self.label = QtGui.QLabel(TestWin)
        self.label.setGeometry(QtCore.QRect(30, 20, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(TestWin)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(TestWin)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(TestWin)
        self.label_6.setGeometry(QtCore.QRect(30, 280, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(TestWin)
        self.label_7.setGeometry(QtCore.QRect(30, 360, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.btnpservos = QtGui.QPushButton(TestWin)
        self.btnpservos.setEnabled(True)
        self.btnpservos.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.btnpservos.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(241, 214, 0);\n"
"border: 1px solid;\n"
"border-radius:2px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(194, 251, 21);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnpservos.setObjectName(_fromUtf8("btnpservos"))
        self.label_2 = QtGui.QLabel(TestWin)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 321, 21))
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(TestWin)
        self.label_3.setGeometry(QtCore.QRect(120, 140, 321, 21))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.btnpfinc = QtGui.QPushButton(TestWin)
        self.btnpfinc.setEnabled(True)
        self.btnpfinc.setGeometry(QtCore.QRect(30, 140, 75, 23))
        self.btnpfinc.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(241, 214, 0);\n"
"border: 1px solid;\n"
"border-radius:2px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(194, 251, 21);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnpfinc.setObjectName(_fromUtf8("btnpfinc"))
        self.lbtraquea = QtGui.QLabel(TestWin)
        self.lbtraquea.setEnabled(True)
        self.lbtraquea.setGeometry(QtCore.QRect(140, 170, 22, 22))
        self.lbtraquea.setStyleSheet(_fromUtf8("background-color: rgb(200, 200, 200);\n"
"border-radius:11px;\n"
""))
        self.lbtraquea.setText(_fromUtf8(""))
        self.lbtraquea.setObjectName(_fromUtf8("lbtraquea"))
        self.lbesofago = QtGui.QLabel(TestWin)
        self.lbesofago.setGeometry(QtCore.QRect(290, 170, 22, 22))
        self.lbesofago.setStyleSheet(_fromUtf8("background-color: rgb(200, 200, 200);\n"
"border-radius:11px;"))
        self.lbesofago.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lbesofago.setText(_fromUtf8(""))
        self.lbesofago.setObjectName(_fromUtf8("lbesofago"))
        self.label_10 = QtGui.QLabel(TestWin)
        self.label_10.setGeometry(QtCore.QRect(200, 240, 141, 21))
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.btnpsharp = QtGui.QPushButton(TestWin)
        self.btnpsharp.setEnabled(True)
        self.btnpsharp.setGeometry(QtCore.QRect(30, 240, 75, 23))
        self.btnpsharp.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(241, 214, 0);\n"
"border: 1px solid;\n"
"border-radius:2px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(194, 251, 21);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnpsharp.setObjectName(_fromUtf8("btnpsharp"))
        self.lcd = QtGui.QLCDNumber(TestWin)
        self.lcd.setGeometry(QtCore.QRect(120, 240, 64, 23))
        self.lcd.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"border: 1px solid;\n"
"border-color:rgb(255, 255, 255);"))
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.btnpev = QtGui.QPushButton(TestWin)
        self.btnpev.setEnabled(True)
        self.btnpev.setGeometry(QtCore.QRect(30, 320, 75, 23))
        self.btnpev.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(241, 214, 0);\n"
"border: 1px solid;\n"
"border-radius:2px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(194, 251, 21);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnpev.setObjectName(_fromUtf8("btnpev"))
        self.label_11 = QtGui.QLabel(TestWin)
        self.label_11.setGeometry(QtCore.QRect(120, 320, 241, 21))
        self.label_11.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(TestWin)
        self.label_12.setGeometry(QtCore.QRect(320, 170, 61, 21))
        self.label_12.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(TestWin)
        self.label_13.setGeometry(QtCore.QRect(170, 170, 61, 21))
        self.label_13.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.btnppulso = QtGui.QPushButton(TestWin)
        self.btnppulso.setEnabled(True)
        self.btnppulso.setGeometry(QtCore.QRect(30, 400, 75, 23))
        self.btnppulso.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(241, 214, 0);\n"
"border: 1px solid;\n"
"border-radius:2px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(194, 251, 21);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnppulso.setObjectName(_fromUtf8("btnppulso"))
        self.label_14 = QtGui.QLabel(TestWin)
        self.label_14.setGeometry(QtCore.QRect(120, 400, 281, 21))
        self.label_14.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.btnpsonido = QtGui.QPushButton(TestWin)
        self.btnpsonido.setEnabled(True)
        self.btnpsonido.setGeometry(QtCore.QRect(30, 480, 75, 23))
        self.btnpsonido.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(241, 214, 0);\n"
"border: 1px solid;\n"
"border-radius:2px;\n"
"border-left-color:rgb(255, 255, 255);\n"
"border-top-color:rgb(255, 255, 255);\n"
"border-right-color:rgb(0, 0, 0);\n"
"border-bottom-color:rgb(0, 0, 0);\n"
" }\n"
"QPushButton:pressed{ \n"
"background-color: rgb(194, 251, 21);\n"
"border-right-color:rgb(100, 100, 100);\n"
"border-bottom-color:rgb(100, 100, 100);\n"
"border-left-color:rgb(100, 100, 100);\n"
"border-top-color:rgb(100, 100, 100);\n"
" }"))
        self.btnpsonido.setObjectName(_fromUtf8("btnpsonido"))
        self.label_8 = QtGui.QLabel(TestWin)
        self.label_8.setGeometry(QtCore.QRect(30, 440, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_15 = QtGui.QLabel(TestWin)
        self.label_15.setGeometry(QtCore.QRect(120, 480, 261, 21))
        self.label_15.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255,0);"))
        self.label_15.setObjectName(_fromUtf8("label_15"))

        self.retranslateUi(TestWin)
        QtCore.QMetaObject.connectSlotsByName(TestWin)

    def retranslateUi(self, TestWin):
        TestWin.setWindowTitle(_translate("TestWin", "Simulador de RCP", None))
        self.label.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Servomotores:</span></p></body></html>", None))
        self.label_4.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Sensores de contacto:</span></p></body></html>", None))
        self.label_5.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Sensor de distancia:</span></p></body></html>", None))
        self.label_6.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Respiración:</span></p></body></html>", None))
        self.label_7.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Motor Pulsos:</span></p></body></html>", None))
        self.btnpservos.setText(_translate("TestWin", "Prueba", None))
        self.label_2.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff7f;\">Observar la apertura y cierre de mandíbula</span></p></body></html>", None))
        self.label_3.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff7f;\">Presione los sensores de intubación (10 s)</span></p></body></html>", None))
        self.btnpfinc.setText(_translate("TestWin", "Prueba", None))
        self.label_10.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff7f;\">Rango (13.5-14.2)</span></p></body></html>", None))
        self.btnpsharp.setText(_translate("TestWin", "Prueba", None))
        self.btnpev.setText(_translate("TestWin", "Prueba", None))
        self.label_11.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff7f;\">Escuchar el sonido de activación</span></p></body></html>", None))
        self.label_12.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffff7f;\">Esófago</span></p></body></html>", None))
        self.label_13.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffff7f;\">Tráquea</span></p></body></html>", None))
        self.btnppulso.setText(_translate("TestWin", "Prueba", None))
        self.label_14.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff7f;\">Sentir cualquier pulso (10 s)</span></p></body></html>", None))
        self.btnpsonido.setText(_translate("TestWin", "Prueba", None))
        self.label_8.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Sonido:</span></p></body></html>", None))
        self.label_15.setText(_translate("TestWin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff7f;\">Escuchar una respiración normal</span></p></body></html>", None))

import Iconos

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TestWin = QtGui.QDialog()
    ui = Ui_TestWin()
    ui.setupUi(TestWin)
    TestWin.show()
    sys.exit(app.exec_())

