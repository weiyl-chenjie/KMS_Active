# Author:尉玉林(Mr.Wei)

# Create Date:2020/03/06

# Edition:V1.0.0

# Python自带库
import re  # 正则表达式
import sys
import subprocess
import winreg  # 操作注册表的库
import platform
# 第三方库
from PySide2.QtWidgets import QMainWindow, QWidget, QApplication
from PySide2.QtGui import Qt
# 自己的包
from UI2PY.MainWindow import Ui_MainWindow
from UI2PY.KMS_Active import Ui_Form as KMS_Active_Form
from UI2PY.OS import Ui_Form as OS_Form


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.Ui_MainWindow = Ui_MainWindow()
        self.Ui_MainWindow.setupUi(self)

        self.KMSActive = KMSActive()
        self.KMSActive.setWindowModality(Qt.ApplicationModal)  # 设置为模态窗口

        self.OS = OS()
        self.OS.setWindowModality(Qt.ApplicationModal)  # 设置为模态窗口

        self.setup()

    def setup(self):
        pass

    # 槽函数
    def kms_active(self):
        self.KMSActive.show()

    def os(self):
        self.OS.show()


class KMSActive(QWidget, KMS_Active_Form):
    def __init__(self):
        super(KMSActive, self).__init__()
        self.PublicFunctions = PublicFunctions()
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.lineEdit_IP.setText('10.40.254.182')

    # 槽函数
    def office_active(self):
        self.textBrowser.setText('正在激活office,请稍后...')
        QApplication.processEvents()
        cwd = self.find_office_path()  # office所在的路径
        # cmd = 'cscript ospp.vbs /sethst:10.40.210.223&cscript ospp.vbs /act'
        cmd = 'cscript ospp.vbs /sethst:' + self.lineEdit_IP.text() + '&cscript ospp.vbs /act'
        # print(cmd)
        res = subprocess.run(cmd, shell=True, capture_output=True, stdin=subprocess.PIPE, cwd=cwd)

        output_str = res.stdout.decode(encoding=("gbk"))
        # print(output_str)
        self.textBrowser.setText(output_str)

    def office_version(self):
        software_name = self.PublicFunctions.find_software()
        keys = software_name.keys()
        text = ''
        self.textBrowser.clear()
        for key in keys:
            if key.startswith('Microsoft Office'):
                # print(key, ":", software_name[key])
                text = text + key + ":" + software_name[key] + '\n'
        self.textBrowser.setText(text)

    def os_active(self):
        self.textBrowser.setText('正在激活操作系统，请稍后...')
        QApplication.processEvents()
        # cmd = r'cd / d "%SystemRoot%\system32"&slmgr /skms 10.40.210.223&slmgr /ato&slmgr /xpr'
        cwd = "%SystemRoot%\system32"
        cmd = r'cd / d "%SystemRoot%\system32"&slmgr /skms ' + self.lineEdit_IP.text() + '&slmgr /ato&slmgr /xpr'
        res = subprocess.run(cmd, shell=True, capture_output=True, stdin=subprocess.PIPE)

        output_str = res.stdout.decode(encoding=("gbk"))
        # print(output_str)
        self.textBrowser.setText(output_str)

    def os_version(self):
        version = platform.win32_ver()
        # print(version)
        self.textBrowser.setText(str(version))

    def set_ip(self):  # 当点击了“设置为当前值”按钮时，ping一下当前IP
        ip = self.lineEdit_IP.text()
        if self.PublicFunctions.is_ip(ip):
            self.textBrowser.setText('Ping一下服务器，请稍后...')
            QApplication.processEvents()
            cmd = r'ping ' + self.lineEdit_IP.text()
            res = subprocess.run(cmd, shell=True, capture_output=True, stdin=subprocess.PIPE)

            output_str = res.stdout.decode(encoding=("gbk"))
            # print(output_str)
            self.textBrowser.setText(output_str)
        else:
            self.textBrowser.setText('输入的不是一个合法的IP')
    # 静态函数
    @staticmethod
    def find_office_path():
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\EXCEL.EXE'
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_key, 0, winreg.KEY_READ)
        value = winreg.QueryValueEx(key, 'Path')
        return value[0]


class OS(QWidget, OS_Form):
    def __init__(self):
        super(OS, self).__init__()
        self.PublicFunctions = PublicFunctions()
        self.setupUi(self)
        self.setup()

    def setup(self):
        pass

    # 槽函数
    def software_list(self):
        software_list = self.PublicFunctions.find_software()
        text = ''
        for key, value in software_list.items():
            text = text + key + '    ' + value + '\n'
        self.textBrowser.setText(text)


class PublicFunctions:
    @staticmethod
    def find_software():
        sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
                   r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']
        software_name = {}  # 软件信息以字典的方式存储，存储格式为‘软件名称’：‘软件版本’
        software_name_sorted = {}  # 排序后的软件信息
        try:
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
        except Exception as ex:
            print(ex)
        # 排序
        for i in sorted(software_name):
            software_name_sorted[i] = software_name[i]

        return software_name_sorted

    @staticmethod
    def is_ip(str_to_confirm):
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if p.match(str_to_confirm):
            return True
        else:
            return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
