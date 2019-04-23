"""
装饰器：
定义：
原则：不能修改被装饰函数的源代码
"""

import  time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func
        stop_time = time.time()
        print("the fun run time is  %s" %(stop_time - start_time))
    return warpper()


# def logger():
#     print('logging')
#
# def test11():
#     pass
#     logger()
#
# def test2():
#     pass
#     logger()
#
# #
@timmer
def test1():
    time.sleep(3)
    print('test1')

test1
