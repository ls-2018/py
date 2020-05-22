### 3. 数据库迁移

在django中继承了makemigrations，可以通过migrate操作去更新数据库，修改我们定义的models，然后在将模型映射到数据库中。

在flask中也有migrate操作，它能跟踪模型的变化，并将变化映射到数据库中

#### 2.1 安装migrate

	pip install flask-migrate

#### 2.2 配置使用migrate

##### 2.2.1 初始化，使用app和db进行migrate对象的初始化

	from flask_migrate import Migrate

	#绑定app和数据库
    Migrate(app=app, db=db)

##### 2.2.2 安装了flask-script的话，可以在Manager()对象上添加迁移指令

	from flask_migrate import Migrate, MigrateCommand

	app = Flask(__name__)

	manage = Manager(app=app)

	manage.add_command('db', MigrateCommand)

操作：

	python manage.py db init  初始化出migrations的文件，只调用一次

	python manage.py db migrate  生成迁移文件

	python manage.py db upgrade 执行迁移文件中的升级
	
	python manage.py db downgrade 执行迁移文件中的降级

	python manage.py db --help 帮助文档
