 
### 1. 开发，页面调试工具debugtoolbar

#### 1.1 安装

	pip install flask-debugtoolbar

#### 1.2 配置

	from flask import Flask

	from flask_debugtoolbar import DebugToolbarExtension
	
	app = Flask(__name__)
	
	app.debug = True
	
	app.config['SECRET_KEY'] = '<replace with a secret key>'
	
	toolbar = DebugToolbarExtension(app)

### 2. restful

Flask-RESTful 提供的最主要的基础就是资源(resources)。资源(Resources)是构建在 Flask 可拔插视图 之上，只要在你的资源(resource)上定义方法就能够容易地访问多个 HTTP 方法

[官网](http://www.pythondoc.com/Flask-RESTful/quickstart.html)上描述了一个最简单的restful风格的api，如下：

	from flask import Flask
	from flask.ext import restful
	
	app = Flask(__name__)
	api = restful.Api(app)
	
	class HelloWorld(restful.Resource):
	    def get(self):
	        return {'hello': 'world'}
	
	api.add_resource(HelloWorld, '/')
	
	if __name__ == '__main__':
	    app.run(debug=True)	


