from django.db import models


class FeedModel(models.Model):
    user_id = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)