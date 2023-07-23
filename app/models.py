from django.db import models

# Create your models here.


class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)


class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Url=models.URLField()
    def __str__(self) -> str:
        return self.Name

class Accessrecord(models.Model):
    Nme=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Date=models.IntegerField(max_length=10)
    Author=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Author