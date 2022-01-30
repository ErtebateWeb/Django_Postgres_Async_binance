from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Exchange(models.Model):
    ExchangeTitle = models.CharField(max_length=100)
    IsDelete = models.BooleanField(default=False)
    IsActive = models.BooleanField(default=True)
    Description = models.CharField(max_length=100)
    CreatedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ExchangeTitle


class Symbol(models.Model):
    title = models.CharField(max_length=30)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.title) + ' on ' + str(self.exchange)
