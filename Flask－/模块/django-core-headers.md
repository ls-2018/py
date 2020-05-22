### 1. 服务器运行跨域配置

#### 1.1 安装 django-cors-headers	

	pip install django-cors-headers	

#### 1.2 添加到已安装的应用程序中

	INSTALLED_APPS  =（
	     ... 
	    ' corsheaders '，
	     ... 
	）

#### 1.3 添加中间件类来收听响应

	MIDDLEWARE  = [
	    ... 
		# 跨域请求中间件
	    'corsheaders.middleware.CorsMiddleware'，
	    ' django.middleware.common.CommonMiddleware'，
	     ... 
	]

#### 1.4 跨域配置

	# 跨域允许的请求方式，可以使用默认值，默认的请求方式为:
	# from corsheaders.defaults import default_methods
	CORS_ALLOW_METHODS = (
	    'GET',
	    'POST',
	    'PUT',
	    'PATCH',
	    'DELETE',
	    'OPTIONS'
	)
	
	# 允许跨域的请求头，可以使用默认值，默认的请求头为:
	# from corsheaders.defaults import default_headers
	# CORS_ALLOW_HEADERS = default_headers

	CORS_ALLOW_HEADERS = (
	    'XMLHttpRequest',
	    'X_FILENAME',
	    'accept-encoding',
	    'authorization',
	    'content-type',
	    'dnt',
	    'origin',
	    'user-agent',
	    'x-csrftoken',
	    'x-requested-with',
	    'Pragma',
	)
	
	# 跨域请求时，是否运行携带cookie，默认为False
	CORS_ALLOW_CREDENTIALS = True
	# 允许所有主机执行跨站点请求，默认为False
	# 如果没设置该参数，则必须设置白名单，运行部分白名单的主机才能执行跨站点请求
	CORS_ORIGIN_ALLOW_ALL = True