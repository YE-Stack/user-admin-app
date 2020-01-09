from os import environ

class AppConfig():
	SECRET_KEY = environ.get('SECRET_KEY') or 'a-7jBACuoyB8qiUedVXvzoBYuuvlNgxPCR_WjH'
