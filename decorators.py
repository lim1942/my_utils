#coding=utf-8
import sys
import time
import threading
from functools import wraps, partial
from traceback import format_tb


class Timeout(Exception):
	pass


class KThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.

        threading.Thread.start(self)

    def __run(self):

        """Hacked run function, which installs the trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace

        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()

        return self.localtrace

    def kill(self):
        self.killed = True



def parse_decorator(return_value):
    """
    :param return_value: catch exceptions when parsing pages, return the default value
    :return: the default value is whatever you want, usually it's 0,'',[],False,{} or None
    """
    def page_parse(func):
        @wraps(func)
        def handle_error(*keys):
            try:
                return func(*keys)
            except Exception as e:
                print('Failed to parse the page, {} is raised, here are details:{}'.format(
                    e, format_tb(e.__traceback__)[0]
                ))
                return return_value

        return handle_error

    return page_parse


# it can be blocked when crawling pages even if we set timeout=out_time in requests.get()
def timeout(seconds):
    def crwal_decorator(func):
        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            # create new args for _new_func, because we want to get the func return val to result list
            new_kwargs = {
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }

            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread

            if alive:
                try:
                    raise Timeout('request timeout')
                finally:
                    return ''
            else:
                if result:
                    return result[0]
                else:
                    return ''
        return wrapper

    return crwal_decorator


def retry(times=-1, delay=0, exceptions=Exception):
    """
    inspired by https://github.com/invl/retry
    :param times: retry times
    :param delay: internals between each retry
    :param exceptions: exceptions may raise in retry
    :return: func result or None
    """
    def _inter_retry(caller, retry_time, retry_delay, es):
        while retry_time:
            try:
                return caller()
            except es as e:
                retry_time -= 1
                if not retry_time:
                    print("max tries for {} times, {} is raised, details: func name is {}, func args are {}".
                                 format(times, e, caller.func.__name__, (caller.args, caller.keywords)))
                    raise
                time.sleep(retry_delay)

    def retry_oper(func):
        @wraps(func)
        def _wraps(*args, **kwargs):
            return _inter_retry(partial(func, *args, **kwargs), times, delay, exceptions)
        return _wraps
    return retry_oper
