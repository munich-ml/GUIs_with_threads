# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_demo(object):
    def setupUi(self, demo):
        demo.setObjectName("demo")
        demo.resize(391, 258)
        self.centralwidget = QtWidgets.QWidget(demo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.spinBoxInput = QtWidgets.QSpinBox(self.frame)
        self.spinBoxInput.setMinimum(0)
        self.spinBoxInput.setMaximum(100)
        self.spinBoxInput.setProperty("value", 33)
        self.spinBoxInput.setObjectName("spinBoxInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinBoxInput)
        self.lineEditResult = QtWidgets.QLineEdit(self.frame)
        self.lineEditResult.setObjectName("lineEditResult")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditResult)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEditTime = QtWidgets.QLineEdit(self.frame)
        self.lineEditTime.setObjectName("lineEditTime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditTime)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonCalcMain = QtWidgets.QPushButton(self.frame_2)
        self.buttonCalcMain.setObjectName("buttonCalcMain")
        self.horizontalLayout.addWidget(self.buttonCalcMain)
        self.buttonCalcWorker = QtWidgets.QPushButton(self.frame_2)
        self.buttonCalcWorker.setObjectName("buttonCalcWorker")
        self.horizontalLayout.addWidget(self.buttonCalcWorker)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        demo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(demo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 26))
        self.menubar.setObjectName("menubar")
        demo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(demo)
        self.statusbar.setObjectName("statusbar")
        demo.setStatusBar(self.statusbar)

        self.retranslateUi(demo)
        QtCore.QMetaObject.connectSlotsByName(demo)

    def retranslateUi(self, demo):
        _translate = QtCore.QCoreApplication.translate
        demo.setWindowTitle(_translate("demo", "QThread demonstrator"))
        self.label_2.setText(_translate("demo", "fibunacci(input)"))
        self.label.setText(_translate("demo", "input"))
        self.label_3.setText(_translate("demo", "compute time [s]"))
        self.buttonCalcMain.setToolTip(_translate("demo", "<html><head/><body><p>the GUI will freeze while computing in main thread</p></body></html>"))
        self.buttonCalcMain.setText(_translate("demo", "compute in main thread"))
        self.buttonCalcWorker.setToolTip(_translate("demo", "<html><head/><body><p>the GUI shouldn\'t freeze while computing in worker thread</p></body></html>"))
        self.buttonCalcWorker.setText(_translate("demo", "compute in worker thread"))

