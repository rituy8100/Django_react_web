from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    contents=models.TextField()
