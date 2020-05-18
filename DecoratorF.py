'''
装饰器文件：
operation_times：参数代表需要执行多少次


'''


def operation_times(number):
    '''装饰器，参数控制需要循环测试的次数'''
    def _operation_times(func):
        def __operation_times(self):
            for i in range(number):
                func(self)
                print('测试执行完成：%s次' %(i+1))
        return __operation_times
    return _operation_times