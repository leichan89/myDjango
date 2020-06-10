# myDjango

使用js等静态文件需要在setting中添加路径

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]