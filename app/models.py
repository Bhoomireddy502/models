from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email = models.EmailField(default='India@gmail.com')
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.author

class Capital(models.Model):
    capital_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.capital_name

class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    capital_name=models.ForeignKey(Capital,on_delete=models.CASCADE,unique=True)
    def __str__(self):
        return self.country_name