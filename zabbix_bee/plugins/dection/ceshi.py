#coding:utf-8
import os

class AppProcess:
	def __init__(self):
		self.status=0
		self.key='ceshi'
		self.check=os.popen('ps -C java -o pid,cmd').readlines()
	def start(self):
		try:
			if len(self.check) < 1:
				print "%s \t***********\033[1;30;41m%s\033[0m" % (self.key,"stop")
				self.status=0
			else:
				print "%s \t----------\033[1;30;42m%s\033[0m" % (self.key,"start")
				self.status=1
		except:
			pass
	def getKey(self):
		return self.key
	def getStatus(self):
		self.start()
		return self.status

def getPluginClass():
	return AppProcess

if __name__ == '__main__':
	test=AppProcess()
	print "-------------------------------"
	test.getStatus()
