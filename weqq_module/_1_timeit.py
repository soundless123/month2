import time
def timeit(f):
    '''
    描述：计算函数执行时间
    语法：timeit(f)() 或装饰器
    :param f:函数
    :return:
    '''
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=f(*args,**kwargs)
        end_time=time.time()
        print("函数执行时间：",end_time-start_time)
        return res
    return wrapper


