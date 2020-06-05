from django.contrib import admin

# 注册表，不注册的话，在访问http://127.0.0.1:8000/admin/时，就看不到表

from . import models

admin.site.register(models.Survey)
admin.site.register(models.ClassList)
admin.site.register(models.SurveyCode)