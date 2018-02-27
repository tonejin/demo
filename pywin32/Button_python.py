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
	
	def OnOK(self):
		win32ui.MessageBox('Press Ok', 'Python', win32con.MB_OK)
		self.EndDialog(1)
	
	def OnCancel(self):
		win32ui.MessageBox('Press Cancel', 'Python', win32con.MB_OK)
		self.EndDialog(1)


style = (win32con.DS_MODALFRAME |
         win32con.WS_POPUP |
         win32con.WS_VISIBLE |
         win32con.WS_CAPTION |
         win32con.WS_SYSMENU |
         win32con.DS_SETFONT)
childstyle = (win32con.WS_CHILD | win32con.WS_VISIBLE)
buttonstyle = win32con.WS_TABSTOP | childstyle
di = ['Python', (0, 0, 300, 180), style, None, (8, 'MS Sans Serif')]
ButOK = (['Button', "OK", win32con.IDOK, (80, 150, 50, 14), buttonstyle | win32con.BS_PUSHBUTTON])
ButCancel = (['Button', "Cancel", win32con.IDCANCEL, (160, 150, 50, 14), buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static', "Python Dialog", 12, (130, 50, 60, 14), childstyle])
Edit = (['Edit', "", 13, (130, 80, 60, 14), childstyle | win32con.ES_LEFT | win32con.WS_BORDER | win32con.WS_TABSTOP])
init = []
init.append(di)
init.append(ButOK)
init.append(ButCancel)
init.append(Stadic)
init.append(Edit)
init.append
mydialog = MyDialog(init)
mydialog.DoModal()
