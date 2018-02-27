#! python3
# _*_ coding:utf-8 _*
# _Author_  : Jin Tone
# _Date_    : 2018/2/24

import win32ui
import win32api
from win32con import *
from pywin.mfc import window
# define windows class
class MyWnd(window.Wnd):
    def __init__(self):
        window.Wnd.__init__(self, win32ui.CreateWnd())
        self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE,\
            win32ui.RegisterWndClass(0, 0, COLOR_WINDOW+1),\
            'MFC GUI', WS_OVERLAPPEDWINDOW,\
            (10, 10, 800, 500), None, 0, None)
        # 捕获右键单击消息
        self.HookMessage(self.OnRClick, WM_RBUTTONDOWN)
    # reload OnClose Method
    def OnClose(self):
        self.EndModalLoop(0)
    # process the RClick event
    def OnRClick(self, param):
        submenu = win32ui.CreatePopupMenu()
        submenu.AppendMenu(MF_STRING, 1054, 'Copy')
        submenu.AppendMenu(MF_STRING, 1055, 'Paste')
        submenu.AppendMenu(MF_SEPARATOR, 1056, None)
        submenu.AppendMenu(MF_STRING, 1057, 'Cut')
        flag = TPM_LEFTALIGN|TPM_LEFTBUTTON|TPM_RIGHTBUTTON
        submenu.TrackPopupMenu(param[5], flag, self)
w = MyWnd()
w.ShowWindow()
w.UpdateWindow()
w.RunModalLoop(1)