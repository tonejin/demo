#! python3
# _*_ coding:utf-8 _*
# @Author   : Jin Tone
# Date      : 2018/2/24

import win32api
import win32con

win32api.MessageBox(win32con.NULL, "Good morning, Fishc!", "操你", win32con.MB_OKCANCEL, win32api.MAKELANGID(win32con.LANG_ENGLISH, win32con.LANG_CHINESE))


