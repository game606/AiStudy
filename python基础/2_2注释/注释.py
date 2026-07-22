print("Hello World") # 单行注释

# print("你好") # 临时屏蔽代码

"""
多行注释
第一行
第二行
第三行
"""

def add(a, b):
    """
    功能：计算两个数的和
    :param a: 第一个加数
    :param b: 第二个加数
    :return: a + b 的结果
    """
    return a + b

# 查看文档注释（验证写法有效）
help(add) # 运行后会输出上面写的文档注释内容