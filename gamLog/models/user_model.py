from django.db import models

# Create your models here.
class UserModel(models.Model):
    userId = models.CharField(max_length=100) #아이디
    pw = models.CharField(max_length=100) #비밀번호
  
