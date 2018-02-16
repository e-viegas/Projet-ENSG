# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_HydroRasterization.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_HydroRasterization(object):
    def setupUi(self, HydroRasterization):
        HydroRasterization.setObjectName("HydroRasterization")
        HydroRasterization.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(HydroRasterization)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(HydroRasterization)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), HydroRasterization.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), HydroRasterization.reject)
        QtCore.QMetaObject.connectSlotsByName(HydroRasterization)

    def retranslateUi(self, HydroRasterization):
        HydroRasterization.setWindowTitle(QtGui.QApplication.translate("HydroRasterization", "HydroRasterization", None, QtGui.QApplication.UnicodeUTF8))
