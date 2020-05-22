#### 2.1 安装


	pip install flask-session

如果指定存session的类型为redis的话，需要安装redis

	pip install redis

#### 2.2 语法

设置session：

	session['key'] = value

读取session：

	result = session['key'] ：如果内容不存在，将会报异常

	result = session.get('key') ：如果内容不存在，将返回None

删除session：

	session.pop('key')

清空session中所有数据：

	session.clear()
	

#### 2.2 使用

我们在初始化文件中创建一个方法，通过调用该方法来获取到Flask的app对象
	
	def create_app():
	    app = Flask(__name__)
	    # SECRET_KEY 秘钥
	    app.config['SECRET_KEY'] = 'secret_key'
		# session类型为redis
	    app.config['SESSION_TYPE'] = 'redis'
		# 添加前缀
    	app.config['SESSION_KEY_PREFIX'] = 'flask'
	    
	    # 加载app的第一种方式
	    se = Session()
	    se.init_app(app=app)
	    #加载app的第二种方式
	    Session(app=app)
	    app.register_blueprint(blueprint=blue)
	
	    return app