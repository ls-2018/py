import tornado.options
import tornado
"""
作用：     
    全局参数的定义、存储、转换
    
"""
tornado.options.define('name', default=None, type=None, help=None, metavar=None,
           multiple=False, group=None, callback=None)

print(tornado.options.options.as_dict())
"""
name                    选项变量名,(唯一)
default=None
type=None               选项类型(int,str,...),从命令行或配置文件导入参数时tornado会类型转换
help=None
metavar=None
multiple=False
group=None
callback=None



用来定义options选项变量的方法

"""