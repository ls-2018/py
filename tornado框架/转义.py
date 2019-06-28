"""
@Time: 2019/6/28 16:48 
@Author: liushuo
@File: 转义.py 
@Desc: 
@Software: PyCharm
"""
# 模板渲染的时候
# {% raw str %}  只有一行不转义

# {% autoescape None%}  整片文档读不转义


"""
在关闭转义的前提下，
{{  escape(str)  }}  对其转义
"""