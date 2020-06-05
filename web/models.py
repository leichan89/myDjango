from django.db import models


class ClassList(models.Model):
    """
    班级表
    """
    name = models.CharField(max_length=32)


class Survey(models.Model):
    """
    问卷调查表
    """
    grade = models.ForeignKey("ClassList", on_delete=models.CASCADE)
    times = models.PositiveSmallIntegerField(verbose_name="第几次")
    # blank=True可以为空
    # ManyToManyField会创建一张中间表，survey_template，有三个字段：id, survey_id, template_id
    survey_template = models.ManyToManyField("SurveyTemplate", blank=True)
    count = models.PositiveSmallIntegerField(verbose_name="生成多少个唯一码")
    date = models.DateTimeField(auto_now_add=True)

class SurveyCode(models.Model):
    """
    唯一码表
    """
    unique_code = models.CharField(max_length=10, unique=True)
    survey = models.ForeignKey("Survey", on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False, verbose_name="是否使用")


class SurveyTemplate(models.Model):
    """
    问卷模板表
    """
    name = models.CharField(max_length=64, help_text="模板名称")


class SurveyQuestion(models.Model):
    """
    问卷问题表
    """
    survey_type_choices = (
        ("choice", "单选"),
        ("suggest", "建议")
    )
    survey_type = models.CharField(max_length=32, choices=survey_type_choices)
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)


class SurveyChoice(models.Model):
    """
    问卷选项表
    """
    question = models.ForeignKey("SurveyQuestion", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    score = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)


class SurveyRecord(models.Model):
    """
    问卷记录
    """
    question = models.ForeignKey("SurveyQuestion", on_delete=models.CASCADE)
    survey_code = models.ForeignKey("SurveyCode", on_delete=models.CASCADE)
    survey = models.ForeignKey("Survey", on_delete=models.CASCADE)
    choice = models.ForeignKey("SurveyChoice", on_delete=models.CASCADE, null=True, blank=True)
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    content = models.CharField(max_length=1024, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
