import os

# __file__ 党委到执行文件的绝对路径
print("__file__", __file__)
# "os.path.abspath(__file__) 格式化绝对路径,让大部分操作都能使用
print("os.path.abspath(__file__):", os.path.abspath(__file__))
# os.path.dirname(os.path.abspath(__file__)) 输出当前执行文件的目录地址
print("os.path.dirname(os.path.abspath(__file__)):", os.path.dirname(os.path.abspath(__file__)))

# 简单的理解方式:app.py中os.path.dirname(os.path.abspath(__file__)) 是定位到当前的工程目录