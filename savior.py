#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import os
import time
from config import DATA_DIR
from .log4spider import get_service_logger


logger = get_service_logger(name='spider_server_service')

if not os.path.isdir(DATA_DIR):
    try:
        os.mkdir(DATA_DIR)
    except Exception as e:
        pass


def _get_date_string():
    return time.strftime("%Y-%m-%d", time.localtime())


def _ensure_data_dir(name):
    data_dir = os.path.join(DATA_DIR, name)
    if not os.path.isdir(data_dir):
        try:
            os.mkdir(data_dir)
        except Exception as e:
            pass
        else:
            return data_dir
    return data_dir


def _ensure_data_dirs(names):
    data_dirs = []
    for name in names:
        data_dir = _ensure_data_dir(name)
        data_dirs.append(data_dir)
    return data_dirs if all(data_dirs) else None


def _processed(data):
    def process_one(j):
        line = []
        for k in sorted(j.keys()):
            v = str(j[k]).replace('^', '').replace('\n', '').replace('~', '') if j[k] else ''
            line.append(v)
        return '^'.join(line)
    if data:
        if isinstance(data, list):
            new_data_string_list = map(process_one, data)
            return new_data_string_list
        elif isinstance(data, dict):
            new_data_string_list = [process_one(data)]
            return new_data_string_list
        else:
            print '!!! error data structure !!!'


class Savior(object):
    def __init__(self, api_class_names):
        global logger
        self.logger = logger
        self.names = api_class_names

        self.date_string = _get_date_string()
        self.fobjs = {}

        self._update_all()

    def _update_all(self):
        if all(self.fobjs.values()):
            try:
                map(lambda f: f.close() if not f.closed else None,
                    self.fobjs.values())
            except Exception, e:
                print e

        self.date_string = _get_date_string()
        self.data_dirs = _ensure_data_dirs(self.names)
        self.fnames = []
        for data_dir in self.data_dirs:
            api_name = data_dir.split(os.sep)[-1]
            fname = self.date_string + '.txt'
            if 'DishonestExecutionInfo' in data_dir:
                self.fnames.extend(
                    [os.path.join(data_dir, api_name + '_' + x + '_' + fname) for x in ['P', 'C']])
            else:
                self.fnames.append(os.path.join(
                    data_dir, api_name + '_' + fname))
        try:
            for fname in self.fnames:
                self.fobjs.update({fname: open(fname, 'a+')})
        except Exception, e:
            print e

    def _ensure_update(self):
        if self.date_string != _get_date_string():
            info = 'Savior object updated all for date {}'
            self.logger.info(info.format(self.date_string))
            self._update_all()
            self.logger.info(info.format(self.date_string))

    def _make_file_name(self, api_class, extra=None):
        class_name = api_class.__class__.__name__
        data_dir = _ensure_data_dir(class_name)
        fname = self.date_string + '.txt'
        if extra:
            fname = extra.upper() + '_' + fname
        fname = class_name + '_' + fname
        fname = os.path.join(data_dir, fname)
        return fname

    def save_new(self, api_class, data, extra=None):
        self._ensure_update()
        self.fname = self._make_file_name(api_class, extra=extra)
        self.fobj = self.fobjs[self.fname]
        new_data_string_list = _processed(data)
        if data and new_data_string_list:
            for new_data in new_data_string_list:
                try:
                    self.fobj.write(new_data + '\n')
                    self.fobj.flush()
                except Exception, e:
                    print e
