from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    body = models.TextField(default='SOME STRING')
    image = models.ImageField(upload_to='images/')