'''
    定义项目中所有对容器的操作。
'''


class ListHelper:
    '''
        列表助手类
    '''

    @staticmethod
    def find_all(iterable_target, func_condition):
        '''
        在可迭代对象中，查找满足条件的所有元素
        :param iterable_target: 可迭代对象
        :param func_condition: 所有条件
        :return: 生成器对象
        '''

        for item in iterable_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable_target, func_condition):
        '''
        在可迭代对象中，查找满足条件的单个元素
        :param iterable_target: 可迭代对象
        :param func_condition: 所有条件
        :return: 元素
        '''

        for item in iterable_target:
            if func_condition(item):
                return item

    @staticmethod
    def sum(iterable_target, func_condition):
        '''
        在可迭代对象中，根据条件求和
        :param iterable_target: 可迭代对象
        :param func_condition: 求和条件
        :return: 去和数值
        '''
        sum_value = 0
        for item in iterable_target:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def select(iterable_target, func_condition):
        '''
         在可迭代对象中，根据条件选择属性
        :param iterable_target: 可迭代对象
        :param func_condition: 筛选条件
        :return: 生成器对象
        '''
        for item in iterable_target:
            yield func_condition(item)

    @staticmethod
    def get_max(iterable_target, func_condition):
        '''
        在可迭代对象中，根据条件获取最大元素
        :param iterable_target: 可迭代对象
        :param func_condition: 获取条件
        :return: 最大元素
        '''

        max_value = iterable_target[0]
        for i in range(1, len(iterable_target)):
            if func_condition(max_value) < func_condition(iterable_target[i]):
                max_value = iterable_target[i]
        return max_value

    @staticmethod
    def order_by(iterable_target, func_condition):
        '''
        对可迭代对象，根据任意条件进行升序排列
        :param iterable_target: 可迭代对象
        :param func_condition: 排序条件
        '''

        for r in range(len(iterable_target) - 1):
            for c in range(r + 1, len(iterable_target)):
                if func_condition(iterable_target[r]) > func_condition(iterable_target[c]):
                    iterable_target[r], iterable_target[c] = iterable_target[c], iterable_target[r]
