# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clientes.ui'
#
# Created: Mon Aug 31 03:03:58 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Cliente(object):
    def setupUi(self, Cliente):
        Cliente.setObjectName("Cliente")
        Cliente.resize(1200, 713)
        self.gridLayout = QtGui.QGridLayout(Cliente)
        self.gridLayout.setObjectName("gridLayout")
        self.table = QtGui.QTableView(Cliente)
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.setObjectName("table")
        self.gridLayout.addWidget(self.table, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(Cliente)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Cliente)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(Cliente)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Cliente)
        QtCore.QMetaObject.connectSlotsByName(Cliente)

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QtGui.QApplication.translate("Cliente", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Cliente", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Cliente", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Cliente", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

