# -*- coding: utf-8 -*-
# @Author: lim
# @Email: 940711277@qq.com
# @Date:  2018-04-10 18:10:42
# @Last Modified by:  lim
# @Last Modified time:  2018-04-10 19:00:51

import time
import uuid
import redis
import traceback
import MySQLdb

R = redis.Redis(host='127.0.0.1', port='7001')
P = R.pipeline(transaction=False)

conn=MySQLdb.connect(host='127.0.0.1',port=3306,db='test'
                ,user='root',passwd='helin4881245',charset='utf8')
cursor=conn.cursor( cursorclass = MySQLdb.cursors.DictCursor )




def save_many_tasks_to_redis(tasks):
    a= time.time()
    for task in tasks:
        task_id = task['task_id']
        task['retry'] = 0
        P.rpush('wx_todo', task_id)
        P.hmset(task_id, task)
    P.execute()
    b = time.time()
    print b-a


def get_20000_tasks_for_redis():

    def generate():
        """a generate to get data line from file"""
        with open('dataset/data_set2/processed_id_name_mobile_no_duplicates.txt') as f:
            for i in xrange(30000):
                f.readline()
            for i in f:
                yield i

    tasks = []
    for line in generate():
        con = line[:-1].split('^')
        idnum = con[0]
        name = con[1]
        phone = con[2]
        task_id = str(uuid.uuid1())
        task = {'task_id':task_id,
                "entrance":['1','2','3'],
                'person':{'name':name,'idnum':idnum,'phone':phone}
                }
        tasks.append(task)
        if len(tasks) == 20000:
            return tasks


def get_20000_tasks_for_mysql():

    def generate():
        """a generate to get data line from file"""
        with open('dataset/data_set2/processed_id_name_mobile_no_duplicates.txt') as f:
            for i in xrange(30000):
                f.readline()
            for i in f:
                yield i

    tasks = []
    for line in generate():
        con = line[:-1].split('^')
        idnum = con[0]
        name = con[1]
        phone = con[2]
        task_id = str(uuid.uuid1())
        task = {'task_id':task_id,
                "entrance":str(['1','2','3']),
                'person':str({'name':name,'idnum':idnum,'phone':phone}),
                'retry':'2',
                'data':'2018-4-23'
                }
        tasks.append(task)
        if len(tasks) == 20000:
            return tasks

def __creat_task_table():
    sql = """CREATE TABLE if not exists task (
             taskid  CHAR(100) NOT NULL primary key,
             entrance   CHAR(200) NOT NULL,  
             person    VARCHAR(400) NOT NULL,
             retry  CHAR(200) NOT NULL,
             data  CHAR(200) NOT NULL,
             fields1 VARCHAR(100),
             fields2 VARCHAR(100))"""
    return cursor.execute(sql)

# __creat_task_table()


def save_many_tasks_to_mysql(tasks):
    print len(tasks)
    a_ = time.time()
    manys = []
    for i,task in enumerate(tasks):
        print i
        a = task['task_id']
        b = task['entrance']
        c = task['person']
        d = task['retry']
        e = task['data']
        manys.append((a,b,c,d,e))
    try:
        sql = """INSERT INTO task(taskid, entrance, person, retry, data)
                 VALUES (%s, %s, %s, %s,%s)"""
        result = cursor.executemany(sql,manys)
        conn.commit()
    except Exception as e:
        traceback.print_exc()
        conn.rollback()        
    b_ = time.time()
    print b_-a_

# save_many_tasks_to_redis(get_20000_tasks_for_redis()) #0.94s
# save_many_tasks_to_mysql(get_20000_tasks_for_mysql()) #13.43s
