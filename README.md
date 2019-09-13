# Python Time Decorator
**A decorator recording running time**  
![](https://img.shields.io/badge/language-python3-blue.svg)
![](https://img.shields.io/badge/license-MIT-green.svg)

## Utility
- [x] decorate function
- [x] decorate Class
- [x] print running time

## Warning
If you use this decorator to decorate a class, it will not record the running time of static methods.  
The way how this decorator ditinguishes different functions is by their names, and ignore which class they belongs to. If you need to record time of functions which have the same name but belongs to different class seperately, feel free to change the source code. (I think only little changes needed)

## Usage
```python
import Timer.py

@timer
def tmp1():
    time.sleep(1)

@timer
def tmp2():
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
    def sleeptest1(self):
        time.sleep(1)

    @staticmethod
    def sleeptest2():
        time.sleep(2)


if __name__ == "__main__":

    tmp1()
    tmp2()
    tmp2()

    t1 = Tester1()
    t1.sleeptest1()
    Tester1.sleeptest2()

    t2 = Tester2()
    t2.sleeptest1()
    Tester2.sleeptest2()

    Timer.show()

```
The results are
```
----------- Time Calculation -----------
Time %     Cumulative sec     self sec     self ocur  single sec   func name
0.47       4.0                4.0          2          2.0          tmp2
0.35       7.01               3.0          2          1.5          sleeptest1
0.12       8.01               1.0          1          1.0          tmp1
0.06       8.51               0.5          1          0.5          sleeptest2
Total time is: 8.51s.
```



# Python Time Decorator
**一个记录代码运行时间的装饰器**

## 功能
- [x] 装饰函数
- [x] 装饰类
- [x] 输出函数运行时间

## 警告
如果你使用此装饰器来装饰类，那么类里的静态成员函数将不会被记录运行时间
此外，装饰器用来区分函数的方式是函数名，而不会理会它们属于的类，如果你需要分开记录两个属于不同类的同名函数的运行时间，请随意修改源码。

## 演示
```python
import Timer.py

@timer
def tmp1():
    time.sleep(1)

@timer
def tmp2():
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
    def sleeptest1(self):
        time.sleep(1)

    @staticmethod
    def sleeptest2():
        time.sleep(2)


if __name__ == "__main__":

    tmp1()
    tmp2()
    tmp2()

    t1 = Tester1()
    t1.sleeptest1()
    Tester1.sleeptest2()

    t2 = Tester2()
    t2.sleeptest1()
    Tester2.sleeptest2()

    Timer.show()

```
结果为
```
----------- Time Calculation -----------
Time %     Cumulative sec     self sec     self ocur  single sec   func name
0.47       4.0                4.0          2          2.0          tmp2
0.35       7.01               3.0          2          1.5          sleeptest1
0.12       8.01               1.0          1          1.0          tmp1
0.06       8.51               0.5          1          0.5          sleeptest2
Total time is: 8.51s.
```
