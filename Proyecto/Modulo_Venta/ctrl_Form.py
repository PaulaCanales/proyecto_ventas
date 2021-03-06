# -*- coding: utf-8 -*-
import sqlite3
from PySide import QtGui, QtCore
from ui_Form_Ventas import Ui_Form
from ui_ventas import Ui_Form as ui_venta
import model as db_model

class FormVenta(QtGui.QDialog):
    fila=0
    def __init__(self, parent=None, folio=None,rut=None):
        """
        Formulario para crear y editar cliente.
        Si se recibe la var folio
        entonces se está en modo de edición.
        """
        super(FormVenta, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.id_prod.activated[int].connect(self.onActivated_idprod)

        if folio is None:
            self.ui.aceptar.setText("Agregar")
            self.ui.venta.setText("Terminar Venta")
            self.ui.guardar.setEnabled(False)
            self.ui.aceptar.clicked.connect(self.crear_venta)
            self.ui.venta.clicked.connect(self.crear_venta2)
            rut= db_model.obtener_rut()
            for dato in range(len(rut)):
                self.ui.comboRut.addItem(str(rut[dato][0]))
            idprod= db_model.obtener_idprod()
            for dato in range(len(idprod)):
                self.ui.id_prod.addItem(str(idprod[dato][0]))
        else:
            self.ui.aceptar.setText("Editar Producto")
            self.ui.venta.setText("Terminar")
            
            
            detalle = db_model.obtener_ventas_formulario(folio)
            self.ui.comboRut.setEnabled(False)
            self.ui.folio.setText(str(folio))
            self.ui.folio.setEnabled(False)
            self.ui.id_prod.setEnabled(False)
            self.ui.cantidad.setEnabled(False)
            self.ui.precio.setEnabled(False)
            #Creamos el modelo asociado a la tabla
            self.data = QtGui.QStandardItemModel(len(detalle), 4)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"producto"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"cantidad"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"precio unitario"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"Total"))
           

            for r, row in enumerate(detalle):
                index = self.data.index(r, 0, QtCore.QModelIndex())
                self.data.setData(index, row['producto_sku'])
                index = self.data.index(r, 1, QtCore.QModelIndex())
                self.data.setData(index, row['cantidad'])
                index = self.data.index(r, 2, QtCore.QModelIndex())
                self.data.setData(index, row['precio_unitario'])
                index = self.data.index(r, 3, QtCore.QModelIndex())
                self.data.setData(index, row['total'])                

            self.ui.grilla_prod.setModel(self.data)

            self.ui.grilla_prod.setColumnWidth(0, 100)
            self.ui.grilla_prod.setColumnWidth(1, 100)
            self.ui.grilla_prod.setColumnWidth(2, 100)
            self.ui.grilla_prod.setColumnWidth(3, 100)

            self.ui.aceptar.clicked.connect(self.carga_venta)
            self.ui.guardar.clicked.connect(self.edita_venta)
            self.ui.venta.clicked.connect(self.cerrar)
            
    def cerrar(self):
        self.close()

    def crear_venta(self): 
        """
        Funcion que crea una venta
        """       
        folio,producto,precio,cantidad=self.obtener_datos()
        try:
            
            db_model.agregar_venta(folio, producto, cantidad, precio)
            detalle = db_model.obtener_ventas_formulario(folio)
            self.ui.comboRut.setEnabled(False)
            self.ui.folio.setText(str(folio))
            self.ui.folio.setEnabled(False)
            
            #Creamos el modelo asociado a la tabla
            self.data = QtGui.QStandardItemModel(len(detalle), 4)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"producto"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"cantidad"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"precio unitario"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"Total"))           

            for r, row in enumerate(detalle):
                index = self.data.index(r, 0, QtCore.QModelIndex())
                self.data.setData(index, row['producto_sku'])
                index = self.data.index(r, 1, QtCore.QModelIndex())
                self.data.setData(index, row['cantidad'])
                index = self.data.index(r, 2, QtCore.QModelIndex())
                self.data.setData(index, row['precio_unitario'])
                index = self.data.index(r, 3, QtCore.QModelIndex())
                self.data.setData(index, row['total'])               

            self.ui.grilla_prod.setModel(self.data)
            
        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error, revise los datos!")
            msgBox.exec_() 

    def crear_venta2(self):
        """
           Funcion que actualiza la grilla de ventas
        """

        rut=int(self.ui.comboRut.currentText ())
        folio = self.ui.folio.text()
        try:
            db_model.crear_venta(int(folio), rut)
            self.accepted.emit()
            self.close()

        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error, revise los datos!")
            msgBox.exec_() 
        

    def carga_venta(self):
        """
        Funcion que carga una venta
        """

        self.ui.cantidad.setEnabled(True)
        self.ui.precio.setEnabled(True)
        data = self.ui.grilla_prod.model()
        index = self.ui.grilla_prod.currentIndex()
        self.fila=self.ui.grilla_prod.currentIndex()
       
        self.ui.cantidad.setText(str(data.index(index.row(), 1, QtCore.QModelIndex()).data()))
        self.ui.precio.setText(str(data.index(index.row(), 2, QtCore.QModelIndex()).data()))
        

    def edita_venta(self): 
        """
        Funcion que edita una venta
        """
        folio = int(self.ui.folio.text())
        detalle = db_model.obtener_ventas_formulario(folio)
        data1 = self.ui.grilla_prod.model()
        index = self.fila
        producto = str(data1.index(index.row(), 0, QtCore.QModelIndex()).data())
        cantidad = int(self.ui.cantidad.text())
        precio = int(self.ui.precio.text())
        
        try:
            
            db_model.editar_venta(folio, producto, cantidad, precio)
            detalle = db_model.obtener_ventas_formulario(folio)
                        
            #Creamos el modelo asociado a la tabla
            self.data = QtGui.QStandardItemModel(len(detalle), 4)
            self.data.setHorizontalHeaderItem(
                0, QtGui.QStandardItem(u"producto"))
            self.data.setHorizontalHeaderItem(
                1, QtGui.QStandardItem(u"cantidad"))
            self.data.setHorizontalHeaderItem(
                2, QtGui.QStandardItem(u"precio unitario"))
            self.data.setHorizontalHeaderItem(
                3, QtGui.QStandardItem(u"Total"))           

            for r, row in enumerate(detalle):
                index = self.data.index(r, 0, QtCore.QModelIndex())
                self.data.setData(index, row['producto_sku'])
                index = self.data.index(r, 1, QtCore.QModelIndex())
                self.data.setData(index, row['cantidad'])
                index = self.data.index(r, 2, QtCore.QModelIndex())
                self.data.setData(index, row['precio_unitario'])
                index = self.data.index(r, 3, QtCore.QModelIndex())
                self.data.setData(index, row['total'])               

            self.ui.grilla_prod.setModel(self.data)
            
        except sqlite3.Error as e: 
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"Error, revise los datos!")
            msgBox.exec_()  


    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        folio = self.ui.folio.text()
        producto = self.ui.id_prod.currentText()
        cantidad = self.ui.cantidad.text()
        precio = self.ui.precio.text()
        return (int(folio),producto,int(precio),int(cantidad))
            

    def onActivated_idprod(self, index):
        """
        Funcion que al seleccionar un idprod (sku)
        escribe automaticamente el precio correspondiente
        """
        idprod = self.ui.id_prod.itemText(index)
        if idprod=="":
            self.ui.precio.setText("")
        else:
            precio = db_model.obtener_precio(idprod)
            self.ui.precio.setText(str(precio))