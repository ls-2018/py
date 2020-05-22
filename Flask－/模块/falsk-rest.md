#### 2.1 安装

	pip install flask_restful

#### 2.2 配置

在create_app()获取Flask(__name__)对象中，设置如下配置

	from flask_restful import Api
	
	api = Api()
	
	api.init_app(app=app)

在views中需要引入配置的api还有Resource
	
	# 导入包和restful中的Api对象
	from flask_restful import Resource
	from utils.functions import api

	# 定义类，启动包含了对数据处理的GET,POST,PATCH,PUT,DELETE请求
	class CreateCourse(Resource):

    def get(self, id):
        course = Course.query.get(id)
        return course.to_dict()

    def post(self):

        courses = ['大学英语', '大学物理', '线性代数', '高数',
                   'VHDL', 'ARM', '马克思主义', '农场劳动']
        course_list = []
        for course in courses:
            c = Course()
            c.c_name = course
            course_list.append(c)
        db.session.add_all(course_list)
        db.session.commit()

        courses = Course.query.all()
        return [course.to_dict() for course in courses]

    def patch(self, id):
        c_name = request.form.get('c_name')
        course = Course.query.get(id)
        course.c_name = c_name
        db.session.commit()
        return {'code': 200, 'data': course.to_dict(), 'msg': '请求成功'}

    def delete(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return {'code': 200, 'msg': '删除成功'}


	# 绑定处理url
	api.add_resource(CreateCourse, '/api/course/<int:id>/', '/api/course/')

#### 2.3 端点(Endpoints)

在一个 API 中，你的资源可以通过多个 URLs 访问。你可以把多个 URLs 传给 Api 对象的 Api.add_resource() 方法。每一个 URL 都能访问到你的 Resource

如：

	api.add_resource(CreateCourse, '/api/course/<int:id>/', '/api/course/')

#### 2.4 返回响应

Flask-RESTful 支持视图方法多种类型的返回值。同 Flask 一样，你可以返回任一迭代器，它将会被转换成一个包含原始 Flask 响应对象的响应。Flask-RESTful 也支持使用多个返回值来设置响应代码和响应头

如：

    def get(self, id):
        course = Course.query.get(id)
        return course.to_dict(), 200