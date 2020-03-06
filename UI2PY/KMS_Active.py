# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KMS_Active.ui',
# licensing of 'KMS_Active.ui' applies.
#
# Created: Fri Mar  6 15:11:43 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton_Office_Active = QtWidgets.QPushButton(Form)
        self.pushButton_Office_Active.setGeometry(QtCore.QRect(60, 40, 93, 28))
        self.pushButton_Office_Active.setObjectName("pushButton_Office_Active")
        self.pushButton_OS_Active = QtWidgets.QPushButton(Form)
        self.pushButton_OS_Active.setGeometry(QtCore.QRect(60, 90, 93, 28))
        self.pushButton_OS_Active.setObjectName("pushButton_OS_Active")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton_Office_Active.setText(QtWidgets.QApplication.translate("Form", "office激活", None, -1))
        self.pushButton_OS_Active.setText(QtWidgets.QApplication.translate("Form", "系统激活", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

