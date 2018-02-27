#! python3
# _*_ coding:utf-8 _*
# @Author   : Jin Tone
"""
一个用python编写的windows服务程序, 监控wps的后台升级程序, 一旦发现立刻杀死!
另外还启动idea_active for Pycharm激活使用. 激活端口: http://localhost:8888
"""

import os
import sys
import time
import win32serviceutil
import win32service
import win32event
import logging
import inspect
import servicemanager
import winerror


class JintoneDeamon(win32serviceutil.ServiceFramework):
	_svc_name_ = "JintoneDeamon"  # 服务名
	_svc_display_name_ = "JintoneDeamon"  # 服务在windows系统中显示的名称
	_svc_description_ = "监控wps的后台升级程序, 一旦发现立刻杀死! 另外还启动idea_active for Pycharm激活使用. 激活端口: http://localhost:8888 "  # 服务的描述
	
	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		self.logger = self._getLogger()
		self.run = True
		self.idea_actived = False
	
	def _getLogger(self):
		logger = logging.getLogger('[JintoneDeamon]')  # "JintoneDeamon"与类名要对应
		
		this_file = inspect.getfile(inspect.currentframe())
		dirpath = os.path.abspath(os.path.dirname(this_file))
		handler = logging.FileHandler(os.path.join(dirpath, "JintoneDeamon_log.txt"))
		
		formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
		handler.setFormatter(formatter)
		
		logger.addHandler(handler)
		logger.setLevel(logging.INFO)
		
		return logger
	
	"""
	实例化win32serviceutil.ServiceFramework的时候，windows系统会自动调用SvcDoRun方法，这个函数的执行不可以结束，因为结束就代表服务停止。所以当我们放自己的代码在SvcDoRun函数中执行的时候，必须确保该函数不退出，类似与这样的效果：
	
	SvcDoRun里实现的是整个服务程序的功能部分

	1 def SvcDoRun(self):
	2        while True:
	3             self._LicenseExist()
	4             time.sleep(2)
	"""
	
	def SvcDoRun(self):  # 方法调用的参数不要增加或修改
		self.logger.info("JintoneDeamon service is running....")
		_wps_services = ("wpsupdate", "updateself", "updsynctool")  # 定义要监控的进程名称
		
		active_file = inspect.getfile(inspect.currentframe())
		active_path = os.path.abspath(os.path.dirname(active_file))
		active_name = (os.path.join(active_path, "idea_active_proxy.exe"))  # idea_active的完整路径
		# 以下是整个服务的功能部分
		while self.run:
			# self.logger.info("I am running....")
			# del_wps_update(self, _wps_services)
			
			# 激活idea_active for Pycharm
			if not self.idea_actived:
				if os.path.exists(active_name):
					self.logger.info("idea_active_proxy.exe now is running....")
					self.idea_actived = True
					os.system(active_name)
				else:
					self.logger.info("%s is not exist!" % active_name)
			
			# 监控wps进程
			for srv in _wps_services:
				# self.logger.info("del_wps_update running")
				result = os.system("sc getdisplayname %s" % srv)
				if result == 0:
					os.system("sc delete %s" % srv)
					self.logger.info("%s deleted!" % srv)
				else:
					pass
			time.sleep(1)
	
	"""
	当停止服务的时候，系统会调用SvcStop函数，该函数通过设置标志位等方式让SvcDoRun函数退出，就是正常的停止服务。
win32event.SetEvent(self.hWaitStop) 通过事件退出
	"""
	
	def SvcStop(self):
		self.logger.info("JintoneDeamon service stopped.")
		os.system("taskkill /im idea_active_proxy.exe -f")  # 强制杀死进程
		time.sleep(3)
		self.logger.info("idea_active_proxy.exe stopped.\n")
		self.idea_actived = False
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)
		self.run = False


if __name__ == '__main__':
	if len(sys.argv) == 1:
		try:
			evtsrc_dll = os.path.abspath(servicemanager.__file__)
			servicemanager.PrepareToHostSingle(JintoneDeamon)
			servicemanager.Initialize('JintoneDeamon', evtsrc_dll)
			servicemanager.StartServiceCtrlDispatcher()
		except win32service.error as details:
			if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
				win32serviceutil.usage()
	else:
		win32serviceutil.HandleCommandLine(JintoneDeamon)

"""
服务操作命令：
#1.安装服务: python JintoneDeamon.py install
#2.让服务自动启动: python JintoneDeamon.py --startup auto install
	--startup: auto delayed manual disabled
#3.启动服务: python JintoneDeamon.py start
#4.重启服务: python JintoneDeamon.py restart
#5.停止服务: python JintoneDeamon.py stop
#6.删除/卸载服务: python JintoneDeamon.py remove
"""
