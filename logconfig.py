#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-28 15:17:02
# @Author  : broono (broono@qq.com)
# @Link    : http://broono.sdf.org
# @Version : $Id$


import os
import logging
from logging.handlers import RotatingFileHandler
from config import gen_log_file_name, LOG_SIZE, LOG_BACKUP


api_logger = None
service_logger = None


def ensure_dir(fname):
    if fname.endswith(os.sep):
        fname = fname.rstrip(os.sep)
    fname = os.path.dirname(fname)
    dirs = fname.split(os.sep)
    for i in range(len(dirs)):
        d = os.sep.join(dirs[:i + 1])
        if not os.path.isdir(d):
            try:
                os.mkdir(d)
            except Exception as e:
                pass


def get_api_logger(name):
    global api_logger
    fname = gen_log_file_name(name)
    ensure_dir(fname)
    if not api_logger:
        api_logger = logging.getLogger(fname)
        # stream_handler = logging.StreamHandler()
        rotating_handler = RotatingFileHandler(
            fname, maxBytes=LOG_SIZE * 1024 * 1024, backupCount=LOG_BACKUP)
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(funcName)-10s %(message)s')
        # stream_handler.setFormatter(formatter)
        rotating_handler.setFormatter(formatter)
        # logger.addHandler(stream_handler)
        api_logger.addHandler(rotating_handler)
        api_logger.setLevel(logging.DEBUG)
    return api_logger


def get_service_logger(name):
    global service_logger
    fname = gen_log_file_name(name)
    ensure_dir(fname)
    if not service_logger:
        service_logger = logging.getLogger(fname)
        # stream_handler = logging.StreamHandler()
        rotating_handler = RotatingFileHandler(
            fname, maxBytes=LOG_SIZE * 1024 * 1024, backupCount=LOG_BACKUP)
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(funcName)-10s %(message)s')
        # stream_handler.setFormatter(formatter)
        rotating_handler.setFormatter(formatter)
        # logger.addHandler(stream_handler)
        service_logger.addHandler(rotating_handler)
        service_logger.setLevel(logging.DEBUG)
    return service_logger
