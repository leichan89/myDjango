# myDjango

使用js等静态文件需要在setting中添加路径，默认存在STATIC_URL

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]