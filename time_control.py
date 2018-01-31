# -*- coding: utf-8 -*-
# @Author: lim
# @Email: 940711277@qq.com
# @Date:  2018-01-31 14:32:23
# @Last Modified by:  lim
# @Last Modified time:  2018-01-31 16:11:39

import os
import time
from multiprocessing import Process


def task(name):
	while 1:
	    print 'Run child process %s (%s)...' % (name, os.getpid())
	    time.sleep(3)

def kill(pid):
	while 1:
		H, M = time.strftime('%H-%M',time.localtime(time.time())).split('-')
		if H == '17':
			os.system('taskkill /pid {} /f'.format(pid))
			break
		time.sleep(5)
	

if __name__ == '__main__':

	while True:
		H, M = time.strftime('%H-%M',time.localtime(time.time())).split('-')
		if H == '16':
			t = Process(target=task, args=('test',))
			t.start()
			pid = t.pid
			k =Process(target=kill,args=(pid,))
			k.start()
			t.join()
		print 'Now is sleeping time,10s,hahaha....'
		time.sleep(10)

