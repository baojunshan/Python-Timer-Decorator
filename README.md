# Python Time Decorator
**一个记录代码运行时间的装饰器**

## 功能
- 可以装饰函数或者类（正在设计中）
- 打印时间

## 演示
```python
@Timer
def tmp():
    time.sleep(1)
    

@Timer
def tmp1():
    time.sleep(2)


if __name__ == "__main__":
    tmp()
    tmp1()
    tmp1()

    # show time
    Timer.show()
```
结果为，
```
----------- Time Calculation -----------
Time %     Cumulative sec     self sec     self ocur  single sec   func name
0.8        4.0                4.0          2          2.0          tmp1
0.2        5.0                1.0          1          1.0          tmp
Total time is: 5.0s.
```

