import os

class AppConfig():
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-7jBACuoyB8qiUedVXvzoBYuuvlNgxPCR_WjH'
