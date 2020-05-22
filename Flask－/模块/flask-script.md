### 4. 修改启动方式，使用命令行参数启动服务

#### 4.1 安装插件


	pip install flask-script

调整代码
	manager = Manager(app=‘自定义的flask对象’)

启动的地方
	manager.run()

#### 4.2 启动命令

	python hellow.py runserver -h 地址 -p 端口 -d -r

其中：-h表示地址。-p表示端口。-d表示debug模式。-r表示自动重启

 



