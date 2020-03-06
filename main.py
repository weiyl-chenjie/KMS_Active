# Author:尉玉林(Mr.Wei)

# Create Date:2020/03/06

# Edition:V1.0.0

# Python自带库
import os
import sys
import winreg  # 操作注册表的库
import platform
# 第三方库
from PySide2.QtWidgets import QMainWindow, QWidget, QApplication
from PySide2.QtGui import Qt
# 自己的包
from UI2PY.MainWindow import Ui_MainWindow
from UI2PY.KMS_Active import Ui_Form as KMS_Active_Form


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.Ui_MainWindow = Ui_MainWindow()
        self.Ui_MainWindow.setupUi(self)

        self.KMSActive = KMSActive()
        self.KMSActive.setWindowModality(Qt.ApplicationModal)  # 设置为模态窗口

        self.setup()

    def setup(self):
        pass

    # 槽函数
    def kms_active(self):
        self.KMSActive.show()



class KMSActive(QWidget, KMS_Active_Form):
    def __init__(self):
        super(KMSActive, self).__init__()
        self.setupUi(self)
        self.setup()

    def setup(self):
        pass

    # 槽函数
    def office_active(self):
        cmd = r'cd /d ' + self.find_office_path()
        cmd = cmd + ' & ' + 'cscript ospp.vbs /sethst:10.40.210.223 & cscript ospp.vbs /act'
        # print(cmd)
        res = os.popen(cmd)
        output_str = res.read()
        # print(output_str)
        self.textBrowser.setText(output_str)

    def office_version(self):
        software_name = self.find_software()
        keys = software_name.keys()
        text = ''
        self.textBrowser.clear()
        for key in keys:
            if key.startswith('Microsoft Office'):
                # print(key, ":", software_name[key])
                text = text + key + ":" + software_name[key] + '\n'
        self.textBrowser.setText(text)

    def os_active(self):
        cmd = r'cd / d "%SystemRoot%\system32" & slmgr /kms 10.40.210.223 & slmgr /ato & slmgr /xpr'
        res = os.popen(cmd)
        output_str = res.read()
        # print(output_str)
        self.textBrowser.setText(output_str)

    def os_version(self):
        version = platform.win32_ver()
        # print(version)
        self.textBrowser.setText(str(version))

    # 静态函数
    @staticmethod
    def find_software():
        sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                   r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']
        software_name = {}  # 软件信息以字典的方式存储，存储格式为‘软件名称’：‘软件版本’
        software_name_sorted = {}  # 排序后的软件信息
        for i in sub_key:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
            for j in range(0, winreg.QueryInfoKey(key)[0] - 1):
                try:
                    key_name = winreg.EnumKey(key, j)
                    key_path = i + '\\' + key_name
                    each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
                    DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayName')
                    DisplayVersion, REG_SZ_ = winreg.QueryValueEx(each_key, 'DisplayVersion')
                    if DisplayName not in software_name.keys():
                        software_name[DisplayName] = DisplayVersion
                except WindowsError:
                    pass
        # 排序
        for i in sorted(software_name):
            software_name_sorted[i] = software_name[i]

        return software_name_sorted

    @staticmethod
    def find_office_path():
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\EXCEL.EXE'
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key, 0, winreg.KEY_READ)
        value = winreg.QueryValueEx(key, 'Path')
        return value[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
