# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KMS_Active.ui',
# licensing of 'KMS_Active.ui' applies.
#
# Created: Fri Mar  6 19:57:35 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 541)
        self.pushButton_Office_Active = QtWidgets.QPushButton(Form)
        self.pushButton_Office_Active.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_Office_Active.setObjectName("pushButton_Office_Active")
        self.pushButton_OS_Active = QtWidgets.QPushButton(Form)
        self.pushButton_OS_Active.setGeometry(QtCore.QRect(30, 70, 93, 28))
        self.pushButton_OS_Active.setObjectName("pushButton_OS_Active")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 140, 671, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_OS_Version = QtWidgets.QPushButton(Form)
        self.pushButton_OS_Version.setGeometry(QtCore.QRect(140, 70, 93, 28))
        self.pushButton_OS_Version.setObjectName("pushButton_OS_Version")
        self.pushButton_Office_Version = QtWidgets.QPushButton(Form)
        self.pushButton_Office_Version.setGeometry(QtCore.QRect(140, 20, 93, 28))
        self.pushButton_Office_Version.setObjectName("pushButton_Office_Version")

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_Office_Active, QtCore.SIGNAL("clicked()"), Form.office_active)
        QtCore.QObject.connect(self.pushButton_OS_Active, QtCore.SIGNAL("clicked()"), Form.os_active)
        QtCore.QObject.connect(self.pushButton_Office_Version, QtCore.SIGNAL("clicked()"), Form.office_version)
        QtCore.QObject.connect(self.pushButton_OS_Version, QtCore.SIGNAL("clicked()"), Form.os_version)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton_Office_Active.setText(QtWidgets.QApplication.translate("Form", "office激活", None, -1))
        self.pushButton_OS_Active.setText(QtWidgets.QApplication.translate("Form", "系统激活", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>", None, -1))
        self.pushButton_OS_Version.setText(QtWidgets.QApplication.translate("Form", "系统版本", None, -1))
        self.pushButton_Office_Version.setText(QtWidgets.QApplication.translate("Form", "office版本", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

