# coding = utf-8
# Author : Bao Junshan (Sanders)
# Date   : 2019-06-19
# Email  : baojunshan123@163.com

import time
import inspect

from functools import wraps


class Timer:
    times = {}

    def __init__(self, obj):

        self.obj = obj
        if inspect.isfunction(self.obj):
            self.obj_type = 'function'
        if inspect.isclass(self.obj):
            self.obj_type = 'class'

    def __call__(self, *args, **kw):
        if self.obj_type == 'function':
            Timer.time_this(self.obj, *args, **kw)
        elif self.obj_type == 'class':
            print(123)

    @staticmethod
    def time_this(func, *args, **kw):
        start_time = time.time()
        func_ret = func(*args, **kw)
        duration = time.time() - start_time
        if func.__name__ in Timer.times.keys():
            Timer.times[func.__name__] = [Timer.times[func.__name__][0] + duration,
                                          Timer.times[func.__name__][1] + 1]
        else:
            Timer.times[func.__name__] = [duration, 1]
        return func_ret

    @staticmethod
    def show():
        print(" Time Calculation ".center(40, "-"))
        if "__total_time__" not in Timer.times.keys():
            Timer.times["__total_time__"] = [sum([i[0] for i in Timer.times.values()]), 1]
        exetime = [[key, value[0], value[1]] for key, value in Timer.times.items()]
        exetime = sorted(exetime, key=lambda x: x[1], reverse=True)
        print("Time %".ljust(10),
              "Cumulative sec".ljust(18),
              "self sec".ljust(12),
              "self ocur".ljust(10),
              "single sec".ljust(12),
              "func name")
        cumulative_time = 0
        for i in exetime:
            if i[0] == "__total_time__":
                continue
            cumulative_time += i[1]
            print(str(round(i[1] / Timer.times["__total_time__"][0], 2)).ljust(10),
                  str(round(cumulative_time, 2)).ljust(18),
                  str(round(i[1], 2)).ljust(12),
                  str(i[2]).ljust(10),
                  str(round(i[1] / i[2], 2)).ljust(12),
                  i[0])
        print("Total time is: {}s.".format(round(Timer.times["__total_time__"][0], 2)))


@Timer
def tmp():
    time.sleep(1)
    print(11111)


@Timer
def tmp1():
    time.sleep(2)


if __name__ == "__main__":

    tmp()
    tmp1()
    tmp1()

    Timer.show()
