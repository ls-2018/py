import tornado.options
import tornado

"""
作用：     
    全局参数的定义、存储、转换
    
"""

tornado.options.define('list', default=[], type=str, help='this is a port info', metavar=None,
                       multiple=True, group=None, callback=None)
"""
name                    选项变量名,(唯一)
default=None
type=None               选项类型(int,float,str,datetime,timedelta),从命令行或配置文件导入参数时tornado会类型转换
                            如果没有设置type，会根据default的值进行转换
                            如果default没有设置，那么不进行转换
help=None               帮助信息
metavar=None
multiple=False          设置选项是否可以为多个值,默认为False,
group=None
callback=None
用来定义options选项变量的方法

"""

# -------------------------------------------------从命令行-------------------------------------------------

# # 获取参数的方法
# tornado.options.parse_command_line()  # 命令行解析
# # python options功能.py --list=123456,456
#
# print(tornado.options.options.as_dict())
# print(tornado.options.options.list)  # ['123456', '456']

# -------------------------------------------------从配置文件-------------------------------------------------
tornado.options.parse_config_file('./conf')  # 格式仍需要按照py的语法格式
# print(tornado.options.options.as_dict())

# -------------------------------------------------从配置文件config.py----------------------------------------
# import config

# print(config.options['port'])
tornado.options.options.logging = None      # 关闭日志功能
