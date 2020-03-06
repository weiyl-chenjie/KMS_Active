# Author:尉玉林(Mr.Wei)

# Create Date:2020/03/06

# Edition:V1.0.0

# Python自带库
import os
# 第三方库
import win32api
import win32con
# 自己的包


def find_office_path():
    sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\EXCEL.EXE'
    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, sub_key, 0, win32con.KEY_READ)
    value = win32api.RegQueryValueEx(key, 'Path')
    return value[0]


def kms_active():
    office_path = find_office_path()
    cmd = r'cd\ & ' + office_path[0:2] + ' & cd ' + find_office_path()
    cmd = cmd + ' & ' + 'cscript ospp.vbs /sethst:10.40.210.223 & cscript ospp.vbs /act'
    # print(cmd)
    res = os.popen(cmd)
    output_str = res.read()
    print(output_str)


if __name__ == '__main__':
    kms_active()
