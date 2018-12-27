import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
'''Question包含一个问题和一个发布日期。
Choice包含两个字段：该选项的文本描述和该选项的投票数。每一条Choice都关联到一个Question。'''
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1)<=self.pub_date<=timezone.now()

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
