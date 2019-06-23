# coding = utf-8
# Author : Bao Junshan (Sanders)
# Date   : 2019-06-19
# Email  : baojunshan123@163.com

import time
import inspect

from functools import wraps, partial

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

class Timer(metaclass=NoInstances):
    times = {}

    @staticmethod
    def time_this(func, *args, **kwargs):
        start_time = time.time()
        func_ret = func(*args, **kwargs)
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

def timer(obj):
    if inspect.isfunction(obj):
        # obj_type = 'function'
        @wraps(obj)
        def wrapper(*args, **kwargs):
            return Timer.time_this(obj, *args, **kwargs)
        return wrapper
    elif inspect.isclass(obj):
        # obj_type = 'class'
        orig_getattribute = obj.__getattribute__
        def new_getattribute(self, name):
            x = orig_getattribute(self, name)
            # print(x.__name__)
            if callable(x):
                return partial(Timer.time_this, x)
            else:
                return x
        obj.__getattribute__ = new_getattribute
        return obj
    else:
        raise Exception("Invalid Decorate type!", obj)


@timer
def tmp():
    time.sleep(1)
    print(11111)


@timer
def tmp1():
    time.sleep(2)

class Tester1:
    @timer
    def sleeptest1(self):
        time.sleep(2)

    @staticmethod
    @timer
    def sleeptest2():
        time.sleep(0.5)

@timer
class Tester2:
    def __init__(self):
        print("Initializing...")
        super().__init__()
        self.x = 0

    def sleeptest1(self):
        time.sleep(1)

    @staticmethod
    def sleeptest2():
        time.sleep(2)


if __name__ == "__main__":

    tmp()
    tmp1()
    tmp1()

    t1 = Tester1()
    t1.sleeptest1()
    Tester1.sleeptest2()

    t2 = Tester2()
    t2.sleeptest1()
    Tester2.sleeptest2()

    Timer.show()
