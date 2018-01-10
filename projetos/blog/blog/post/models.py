from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()
    # author = models.ForeignKey(
    #    'core.User',
    #    on_delete=models.CASCADE
    #)
