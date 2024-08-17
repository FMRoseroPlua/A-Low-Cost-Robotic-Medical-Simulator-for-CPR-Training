# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Mio\Espe\Tesis\Interfaz\Interfaz_RCP\GUIs\EscgWin.ui'
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

class Ui_EscgWin(object):
    def setupUi(self, EscgWin):
        EscgWin.setObjectName(_fromUtf8("EscgWin"))
        EscgWin.resize(650, 450)
        EscgWin.setMinimumSize(QtCore.QSize(650, 450))
        EscgWin.setMaximumSize(QtCore.QSize(840, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/main/Icono.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EscgWin.setWindowIcon(icon)
        EscgWin.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(53, 50, 48, 255), stop:1 rgba(97, 91, 88, 255));\n"
""))
        self.graphicsView = PlotWidget(EscgWin)
        self.graphicsView.setGeometry(QtCore.QRect(80, 30, 400, 261))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.label = QtGui.QLabel(EscgWin)
        self.label.setGeometry(QtCore.QRect(100, 320, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.medidor = QtGui.QProgressBar(EscgWin)
        self.medidor.setGeometry(QtCore.QRect(530, 30, 41, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.medidor.setFont(font)
        self.medidor.setStyleSheet(_fromUtf8("\n"
"border:1px solid;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);"))
        self.medidor.setProperty("value", 0)
        self.medidor.setOrientation(QtCore.Qt.Vertical)
        self.medidor.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.medidor.setObjectName(_fromUtf8("medidor"))
        self.label_2 = QtGui.QLabel(EscgWin)
        self.label_2.setGeometry(QtCore.QRect(100, 360, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(EscgWin)
        self.label_3.setGeometry(QtCore.QRect(100, 400, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lbfrecuencia = QtGui.QLabel(EscgWin)
        self.lbfrecuencia.setEnabled(True)
        self.lbfrecuencia.setGeometry(QtCore.QRect(240, 320, 111, 21))
        self.lbfrecuencia.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167);\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel:hover{ background-color: white; }"))
        self.lbfrecuencia.setText(_fromUtf8(""))
        self.lbfrecuencia.setObjectName(_fromUtf8("lbfrecuencia"))
        self.lbtiempo = QtGui.QLabel(EscgWin)
        self.lbtiempo.setGeometry(QtCore.QRect(240, 360, 111, 21))
        self.lbtiempo.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color: rgb(244, 255, 167);\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel:hover{ background-color: white; }"))
        self.lbtiempo.setText(_fromUtf8(""))
        self.lbtiempo.setObjectName(_fromUtf8("lbtiempo"))
        self.lbresultado = QtGui.QLabel(EscgWin)
        self.lbresultado.setGeometry(QtCore.QRect(240, 400, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbresultado.setFont(font)
        self.lbresultado.setStyleSheet(_fromUtf8("QLabel{ \n"
"background-color:rgb(244, 255, 167);\n"
"color: rgb(0, 0, 0);\n"
"border:1px solid;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QLabel:hover{ background-color: white; }"))
        self.lbresultado.setText(_fromUtf8(""))
        self.lbresultado.setObjectName(_fromUtf8("lbresultado"))
        self.btnresultados = QtGui.QPushButton(EscgWin)
        self.btnresultados.setEnabled(False)
        self.btnresultados.setGeometry(QtCore.QRect(420, 340, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnresultados.setFont(font)
        self.btnresultados.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(255, 164, 16);\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Botones/res1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnresultados.setIcon(icon1)
        self.btnresultados.setIconSize(QtCore.QSize(15, 15))
        self.btnresultados.setObjectName(_fromUtf8("btnresultados"))
        self.btndetalle = QtGui.QPushButton(EscgWin)
        self.btndetalle.setEnabled(False)
        self.btndetalle.setGeometry(QtCore.QRect(420, 380, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btndetalle.setFont(font)
        self.btndetalle.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(255, 164, 16);\n"
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
        self.btndetalle.setIcon(icon1)
        self.btndetalle.setIconSize(QtCore.QSize(15, 15))
        self.btndetalle.setObjectName(_fromUtf8("btndetalle"))

        self.retranslateUi(EscgWin)
        QtCore.QMetaObject.connectSlotsByName(EscgWin)

    def retranslateUi(self, EscgWin):
        EscgWin.setWindowTitle(_translate("EscgWin", "Simulador de RCP", None))
        self.label.setText(_translate("EscgWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Frecuencia:</span></p></body></html>", None))
        self.label_2.setText(_translate("EscgWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Tiempo:</span></p></body></html>", None))
        self.label_3.setText(_translate("EscgWin", "<html><head/><body><p><span style=\" font-size:14pt; color:#fbfbfb;\">Resultado:</span></p></body></html>", None))
        self.btnresultados.setText(_translate("EscgWin", "Resultados", None))
        self.btndetalle.setText(_translate("EscgWin", "Detalle", None))

from pyqtgraph import PlotWidget
import Iconos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EscgWin = QtGui.QDialog()
    ui = Ui_EscgWin()
    ui.setupUi(EscgWin)
    EscgWin.show()
    sys.exit(app.exec_())

