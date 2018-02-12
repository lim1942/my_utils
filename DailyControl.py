# -*- coding: utf-8 -*-
# @Author: lim
# @Email: 940711277@qq.com
# @Date:  2018-01-31 14:32:23
# @Last Modified by:  lim
# @Last Modified time:  2018-02-12 11:47:22

import os
import time
from multiprocessing import Process


def kill(pid,stop):
	"""killer，用于终止任务的函数"""
	while True:
		H, M = time.strftime('%H-%M').split('-')
		if H+M == stop:
			a= os.system('taskkill /pid {} /f > NUL'.format(pid))
			if a ==0:
				print('{}--has been killed'.format(pid))
				break
		print('>>>>>>task func will stop at {}:{}'.format(stop[0:2],stop[2:]))
		time.sleep(30)
	


def DailyControl(start,stop,task,args=None,weekly=False):

	"""
	利用多进程实现的定时器，控制任务函数每天的启停。
	参数说明：
		start:0900 每天的启动时间
		stop:2100 每天的停止时间
		task:func 传入被控制的函数（服务入口）
		args:(,) 任务函数需要传入的参数
		weeklk:false 是否只在工作日执行服务
	"""

	print ('now is {}'.format(time.strftime('%Y-%m-%d-%H:%M:%S')))
	print('>>>>>>task func will start at {}:{}'.format(start[0:2],start[2:]))

	while True:

		#get week,hour,minute for control
		w,H, M = time.strftime('%w-%H-%M').split('-')
		if H+M == start:

			#not weekday process won`t be start
			if weekly:
				if w not in '12345':
					print('today is weekend---')
					time.sleep(30)
					continue

			#process start
			if args:
				t = Process(target=task,args=args)
			else:
				t = Process(target=task)
			t.start()
			pid = t.pid

			#run a killer to kill task in the right time
			k = Process(target=kill,args=(pid,stop))
			k.start()
			k.join()

		print('Now is sleeping time,hahaha...')
		time.sleep(30)


if __name__ == '__main__':
	
	def test():
		while True:
	    		print('Run task process (%s)...' % (os.getpid()))
	    		time.sleep(3)

	DailyControl('1147','1148',test)
