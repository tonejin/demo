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
		self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE, \
		                          win32ui.RegisterWndClass(0, 0, COLOR_WINDOW + 1), \
		                          'MFC GUI', WS_OVERLAPPEDWINDOW, \
		                          (10, 10, 800, 500), None, 0, None)
		# 捕获右键单击消息
		submenu = win32ui.CreatePopupMenu()
		menu = win32ui.CreateMenu()
		submenu.AppendMenu(MF_STRING, 1051, '&Open')
		submenu.AppendMenu(MF_STRING, 1052, '&Close')
		submenu.AppendMenu(MF_STRING, 1053, '&Save')
		menu.AppendMenu(MF_STRING | MF_POPUP, submenu.GetHandle(), '&File')
		submenu = win32ui.CreateMenu()
		submenu.AppendMenu(MF_STRING, 1054, '&Copy')
		submenu.AppendMenu(MF_STRING, 1055, '&Paste')
		submenu.AppendMenu(MF_SEPARATOR, 1056, None)
		submenu.AppendMenu(MF_STRING, 1057, '&Cut')
		menu.AppendMenu(MF_STRING | MF_POPUP, submenu.GetHandle(), '&Edit')
		submenu = win32ui.CreateMenu()
		submenu.AppendMenu(MF_STRING, 1058, 'Tools')
		submenu.AppendMenu(MF_STRING | MF_GRAYED, 1059, 'Setting')
		m = win32ui.CreateMenu()
		m.AppendMenu(MF_STRING | MF_POPUP | MF_CHECKED, submenu.GetHandle(), 'Option')
		menu.AppendMenu(MF_STRING | MF_POPUP, m.GetHandle(), '&Other')
		self._obj_.SetMenu(menu)
	
	# reload OnClose Method
	def OnClose(self):
		self.EndModalLoop(0)
	# process the RClick event


w = MyWnd()
w.ShowWindow()
w.UpdateWindow()
w.RunModalLoop(1)
