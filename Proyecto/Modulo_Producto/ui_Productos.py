# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Productos.ui'
#
# Created: Sun Aug 30 00:26:54 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(1200, 633)
        self.gridLayout = QtGui.QGridLayout(Productos)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Productos)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.combosku = QtGui.QComboBox(Productos)
        self.combosku.setEditable(True)
        self.combosku.setObjectName("combosku")
        self.combosku.addItem("")
        self.combosku.setItemText(0, "")
        self.gridLayout.addWidget(self.combosku, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Productos)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buscar = QtGui.QPushButton(Productos)
        self.buscar.setObjectName("buscar")
        self.horizontalLayout.addWidget(self.buscar)
        self.agregar = QtGui.QPushButton(Productos)
        self.agregar.setObjectName("agregar")
        self.horizontalLayout.addWidget(self.agregar)
        self.editar = QtGui.QPushButton(Productos)
        self.editar.setObjectName("editar")
        self.horizontalLayout.addWidget(self.editar)
        self.eliminar = QtGui.QPushButton(Productos)
        self.eliminar.setObjectName("eliminar")
        self.horizontalLayout.addWidget(self.eliminar)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.grilla_prod = QtGui.QTableView(Productos)
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")
        self.gridLayout.addWidget(self.grilla_prod, 4, 0, 1, 4)
        self.img = QtGui.QLabel(Productos)
        self.img.setEnabled(True)
        self.img.setMinimumSize(QtCore.QSize(100, 100))
        self.img.setMaximumSize(QtCore.QSize(100, 100))
        self.img.setText("")
        self.img.setScaledContents(False)
        self.img.setWordWrap(True)
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 0, 3, 4, 1)
        self.label_2 = QtGui.QLabel(Productos)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.combonombre = QtGui.QComboBox(Productos)
        self.combonombre.setEditable(True)
        self.combonombre.setObjectName("combonombre")
        self.combonombre.addItem("")
        self.combonombre.setItemText(0, "")
        self.gridLayout.addWidget(self.combonombre, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)
        Productos.setTabOrder(self.combosku, self.combonombre)
        Productos.setTabOrder(self.combonombre, self.editar)
        Productos.setTabOrder(self.editar, self.eliminar)
        Productos.setTabOrder(self.eliminar, self.grilla_prod)

    def retranslateUi(self, Productos):
        Productos.setWindowTitle(QtGui.QApplication.translate("Productos", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Productos", "BUSQUEDA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Productos", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.buscar.setText(QtGui.QApplication.translate("Productos", "Actualizar", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar.setText(QtGui.QApplication.translate("Productos", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.editar.setText(QtGui.QApplication.translate("Productos", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Productos", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Productos", "Código", None, QtGui.QApplication.UnicodeUTF8))

