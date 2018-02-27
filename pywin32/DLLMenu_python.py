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
        # create menu object
        submenu = win32ui.CreatePopupMenu()
        menu = win32ui.CreateMenu()
        # add sth into menu
        submenu.AppendMenu(MF_STRING, 1051,'&Open')
        submenu.AppendMenu(MF_STRING, 1052,'&Close')
        submenu.AppendMenu(MF_STRING, 1053,'&Save')
        menu.AppendMenu(MF_STRING|MF_POPUP,submenu.GetHandle(),'&File')
        # add menu into window
        self._obj_.SetMenu(menu)
        # set menu process message
        self.HookCommand(self.MenuClick, 1051)
        self.HookCommand(self.MenuClick, 1052)
        self.HookCommand(self.MenuClick, 1053)
    # reload OnClose Method
    def OnClose(self):
        self.EndModalLoop(0)
    def MenuClick(self, lParam, wParam):
        if lParam == 1051:
            self.MessageBox('Open', 'Python', MB_OK)
        elif lParam == 1053:
            self.MessageBox('Save', 'Python', MB_OK)
        else:
            self.OnClose()
w = MyWnd()
w.ShowWindow()
w.UpdateWindow()
w.RunModalLoop(1)