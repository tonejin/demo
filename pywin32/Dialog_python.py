#! python3
# _*_ coding:utf-8 _*
# _Author_  : Jin Tone
# _Date_    : 2018/2/24
import win32ui
import win32con
from pywin.mfc import dialog


# define windows class
class MyDialog(dialog.Dialog):
	def OnInitDialog(self):
		dialog.Dialog.OnInitDialog(self)


style = (win32con.DS_MODALFRAME |
         win32con.WS_POPUP |
         win32con.WS_VISIBLE |
         win32con.WS_CAPTION |
         win32con.WS_SYSMENU |
         win32con.DS_SETFONT)
di = ['Python',
      (0, 0, 300, 180),
      style,
      None,
      (8, 'MS Sans Serif')]
init = []
init.append(di)
mydialog = MyDialog(init)
mydialog.DoModal()
