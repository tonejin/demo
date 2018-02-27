#! python3
# _*_ coding:utf-8 _*
# @Author   : Jin Tone
"""
一个用python编写的windows服务程序, 用来激活pycharm!
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


class idea_active(win32serviceutil.ServiceFramework):
	_svc_name_ = "idea_active"  # 服务名
	_svc_display_name_ = "idea_active"  # 服务在windows系统中显示的名称
	_svc_description_ = "This is a python service to idea_active "  # 服务的描述
	_exe_name_ = "idea_active"
	
	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		self.logger = self._getLogger()
		self.run = True
	
	def _getLogger(self):
		logger = logging.getLogger('[idea_active]')  # "PythonService"与类名要对应
		
		this_file = inspect.getfile(inspect.currentframe())
		dirpath = os.path.abspath(os.path.dirname(this_file))
		handler = logging.FileHandler(os.path.join(dirpath, "idea_active_log.txt"))
		
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
	
	def SvcDoRun(self):  # 方法调用的参数不要增加
		self.logger.info("service is running....")
		# 以下是整个服务的功能部分
		while self.run:
			# self.logger.info("I am running....")
			exe_name = (os.path.join(dirpath, "idea_active_proxy.exe"))
			# self.logger.info("del_wps_update running")
			result = os.system("sc getdisplayname idea_active")
			if result != 0:
				if not FileExistsError(exe_name):
					result = os.system(exe_name)
				else:
					self.logger.info("%s is not exist!" %exe_name)
			time.sleep(5)
	
	"""
	当停止服务的时候，系统会调用SvcStop函数，该函数通过设置标志位等方式让SvcDoRun函数退出，就是正常的停止服务。
win32event.SetEvent(self.hWaitStop) 通过事件退出
	"""
	
	def SvcStop(self):
		self.logger.info("service is stop....")
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)
		self.run = False


# def del_wps_update(self, _wps_services):
# 	for srv in _wps_services:
# 		result = os.system("sc getdisplayname %s" % srv)
# 		print("del_wps_update running \n")
# 		if result == 0:
# 			message = os.system("sc delete %s" % srv)
# 		else:
# 			pass

# while True:
# 	del_wps_update(_wps_services)
# 	time.sleep(1)


if __name__ == '__main__':
	if len(sys.argv) == 1:
		try:
			evtsrc_dll = os.path.abspath(servicemanager.__file__)
			servicemanager.PrepareToHostSingle(idea_active)
			servicemanager.Initialize('idea_active', evtsrc_dll)
			servicemanager.StartServiceCtrlDispatcher()
		except win32service.error as details:
			if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
				win32serviceutil.usage()
	else:
		win32serviceutil.HandleCommandLine(idea_active)

"""
服务操作命令：
#1.安装服务: python PythonService.py install
#2.让服务自动启动: python PythonService.py --startup auto install
#3.启动服务: python PythonService.py start
#4.重启服务: python PythonService.py restart
#5.停止服务: python PythonService.py stop
#6.删除/卸载服务: python PythonService.py remove
"""
