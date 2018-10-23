from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=32)  #md5 code 32bit
    user_email = models.CharField(max_length=30)
    receive_name = models.CharField(max_length=20, default='')
    receive_addr = models.CharField(max_length=30, default='')
    receive_phone = models.CharField(max_length=11, default='')
    receive_postcode = models.CharField(max_length=6, default='')

    def __str__(self):
        return self.user_name


