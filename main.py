from PyQt5.QtWidgets import QApplication
import win32gui
import sys
import time
import os

hwnd_title = dict()
winId = None


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

print('-----------系统运行中窗体句柄列表-----------')
for h, t in hwnd_title.items():
    if t != "":
        print('[+] ' + str(h) + " -- " + t)

    if '钉钉' in t:
        winId = h

print('-----------系统运行中窗体句柄列表-----------')

if winId == None:
    print('[×] 未发现目标窗口句柄, 程序终止运行...')
    sys.exit()

app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
root_path = 'C:\\Users\\genqing.yang\\Desktop\\screenShot\\'
if not os.path.exists(root_path):
    os.mkdir(root_path)

print('[+] 程序运行中...')

while True:
    file_name = root_path + \
        time.strftime('%Y%m%d%H%M%S', time.localtime()) + ".jpg"
    img = screen.grabWindow(winId).toImage()
    img.save(file_name)
    time.sleep(1)
