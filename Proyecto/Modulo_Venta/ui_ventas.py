# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventas.ui'
#
# Created: Mon Aug 31 03:34:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 713)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.filtro = QtGui.QComboBox(Form)
        self.filtro.setEditable(True)
        self.filtro.setObjectName("filtro")
        self.filtro.addItem("")
        self.filtro.setItemText(0, "")
        self.verticalLayout.addWidget(self.filtro)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vender = QtGui.QPushButton(Form)
        self.vender.setObjectName("vender")
        self.horizontalLayout.addWidget(self.vender)
        self.editar = QtGui.QPushButton(Form)
        self.editar.setObjectName("editar")
        self.horizontalLayout.addWidget(self.editar)
        self.eliminar = QtGui.QPushButton(Form)
        self.eliminar.setObjectName("eliminar")
        self.horizontalLayout.addWidget(self.eliminar)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.comboProv = QtGui.QComboBox(Form)
        self.comboProv.setEditable(True)
        self.comboProv.setObjectName("comboProv")
        self.comboProv.addItem("")
        self.comboProv.setItemText(0, "")
        self.gridLayout_2.addWidget(self.comboProv, 3, 1, 1, 1)
        self.comboFolio = QtGui.QComboBox(Form)
        self.comboFolio.setEditable(True)
        self.comboFolio.setObjectName("comboFolio")
        self.comboFolio.addItem("")
        self.comboFolio.setItemText(0, "")
        self.gridLayout_2.addWidget(self.comboFolio, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.fecha = QtGui.QDateEdit(Form)
        self.fecha.setWrapping(False)
        self.fecha.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 8, 29), QtCore.QTime(0, 0, 0)))
        self.fecha.setMinimumTime(QtCore.QTime(3, 0, 0))
        self.fecha.setCalendarPopup(True)
        self.fecha.setObjectName("fecha")
        self.gridLayout_2.addWidget(self.fecha, 1, 1, 1, 1)
        self.sinFiltro = QtGui.QPushButton(Form)
        self.sinFiltro.setObjectName("sinFiltro")
        self.gridLayout_2.addWidget(self.sinFiltro, 4, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.grilla_prod = QtGui.QTableView(Form)
        self.grilla_prod.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.grilla_prod.setAlternatingRowColors(True)
        self.grilla_prod.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.grilla_prod.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.grilla_prod.setSortingEnabled(True)
        self.grilla_prod.setObjectName("grilla_prod")
        self.gridLayout.addWidget(self.grilla_prod, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.grilla_prod, self.vender)
        Form.setTabOrder(self.vender, self.editar)
        Form.setTabOrder(self.editar, self.eliminar)
        Form.setTabOrder(self.eliminar, self.fecha)
        Form.setTabOrder(self.fecha, self.comboProv)
        Form.setTabOrder(self.comboProv, self.comboFolio)
        Form.setTabOrder(self.comboFolio, self.filtro)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "FILTRO", None, QtGui.QApplication.UnicodeUTF8))
        self.vender.setText(QtGui.QApplication.translate("Form", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.editar.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "BUSQUEDA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.sinFiltro.setText(QtGui.QApplication.translate("Form", "Sin Filtro", None, QtGui.QApplication.UnicodeUTF8))

