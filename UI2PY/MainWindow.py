# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Fri Mar  6 15:11:47 2020
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(310, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 141, 95, 135))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_KMS_Active = QtWidgets.QPushButton(self.widget)
        self.pushButton_KMS_Active.setObjectName("pushButton_KMS_Active")
        self.verticalLayout.addWidget(self.pushButton_KMS_Active)
        self.pushButton_Office = QtWidgets.QPushButton(self.widget)
        self.pushButton_Office.setObjectName("pushButton_Office")
        self.verticalLayout.addWidget(self.pushButton_Office)
        self.pushButton_System = QtWidgets.QPushButton(self.widget)
        self.pushButton_System.setObjectName("pushButton_System")
        self.verticalLayout.addWidget(self.pushButton_System)
        self.pushButton_Other = QtWidgets.QPushButton(self.widget)
        self.pushButton_Other.setObjectName("pushButton_Other")
        self.verticalLayout.addWidget(self.pushButton_Other)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_KMS_Active, QtCore.SIGNAL("clicked()"), MainWindow.kmsActive)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_Title.setText(QtWidgets.QApplication.translate("MainWindow", "工具百宝箱", None, -1))
        self.pushButton_KMS_Active.setText(QtWidgets.QApplication.translate("MainWindow", "KMS激活", None, -1))
        self.pushButton_Office.setText(QtWidgets.QApplication.translate("MainWindow", "Office工具", None, -1))
        self.pushButton_System.setText(QtWidgets.QApplication.translate("MainWindow", "操作系统", None, -1))
        self.pushButton_Other.setText(QtWidgets.QApplication.translate("MainWindow", "其它", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

