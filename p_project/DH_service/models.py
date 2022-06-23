from django.db import models

# Create your models here.

# 검색어와 검색 기간을 입력하면 이곳으로 저장
class SEND_DATA(models.Model):
    text = models.CharField(max_length=10)
    start_day = models.DateField()
    end_day = models.DateField()
    def __str__(self):
        return self.text
