from django.dispatch import receiver

from django.db.models.signals import post_save

# get_random_string 获取随机数的string
from django.utils.crypto import get_random_string

from .. import models


@receiver(post_save, sender=models.Survey)
def create_unique_code(**kwargs):
    """
    http://127.0.0.1:8000/admin/web/survey/重复创建Survey的时候，create字段会变为False
    {
        'signal': <django.db.models.signals.ModelSignal object at 0x10c5aa4a8>,
        'sender': <class 'web.models.Survey'>,
        'instance': <Survey: Survey object (1)>,
        'created': True,
        'update_fields': None,
        'raw': False,
        'using': 'default'
    }
    """
    created = kwargs.get("created", False)
    if not created:
        return

    instance = kwargs.get("instance")

    count = instance.count
    codes = []
    while count:
        _code = get_random_string(8)
        if models.SurveyCode.objects.filter(unique_code=_code).exists():
            continue
        # 将SurveyCode对象添加到一个列表中，便于后面批量创建
        codes.append(models.SurveyCode(unique_code=_code, survey=instance))
        count -= 1
    models.SurveyCode.objects.bulk_create(codes)