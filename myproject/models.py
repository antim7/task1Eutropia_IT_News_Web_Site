from django.db import models

# Create your models here.
class Createnews(models.Model):
    NewsId = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=150)
    NewsDetails = models.TextField()
    Coverimage = models.ImageField(upload_to='images')





