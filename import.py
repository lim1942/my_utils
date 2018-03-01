#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-10 11:00:20
# @Author  : broono (broono@qq.com)
# @Link    : http://broono.sdf.org
# @Version : $Id$

import gevent
from gevent import monkey
monkey.patch_all()
import os
from importlib import import_module
from config import P2P_REGISTER_QUERY_TIMEOUT
from utils.log4spider import get_service_logger
import sys
reload(sys)
sys.setdefaultencoding('utf8')


service_logger = get_service_logger(name='spider_server_service')
modules = []

_base = os.path.dirname(__file__)
_dirs = ['not_need_captcha', 'bypass_need_captcha', 'pissed_mixin']
for root, dirs, files in os.walk(_base):
    for file in files:
        if  any(map(lambda _dir: True if _dir in root else False, _dirs)):
            if file.endswith('.py') and not file.startswith('_'):
                cpath = '.'.join(root.split(os.sep)[root.split(os.sep).index('interfaces'):])
                _mod_name = '.'.join([cpath, file[:-3]])
                _package = import_module(_mod_name, package=root)
                modules.append(_package)


def _reflect(module):
    for attrib in dir(module):
        attribute = getattr(module, attrib)
        if 'getMessage' in dir(attribute):
            instance = attribute(to=P2P_REGISTER_QUERY_TIMEOUT)
            if instance:
                return instance


validators = map(_reflect, modules)

print '{} portals dynamically loaded'.format(len(validators))


def get_restful_from_p2pregister(mobile):
    global validators, service_logger
    tasks = [gevent.spawn(validator.getMessage, mobile) for validator in validators]
    gevent.joinall(tasks, timeout=max(P2P_REGISTER_QUERY_TIMEOUT, 1000))
    yes, no, unknown = [], [], []
    for task in tasks:
        task = task.value
        if task:
            if task['status'] == '1':
                yes.append(task)
            elif task['status'] == '0':
                no.append(task)
            elif task['status'] == '-1':
                unknown.append(task)
                service_logger.error('{} {} {} {}'.format(task['name'], task['url'], task['status'], task['reason']))
        else:
            service_logger.error('return unexpected None in function')
    for y in yes:
        del y['status']
        del y['reason']
    print yes
    return yes


__all__ = ['get_restful_from_p2pregister']
