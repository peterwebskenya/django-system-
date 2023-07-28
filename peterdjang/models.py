from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.IntegerField(default=1)
    country = models.CharField(default='kenya', max_length=30)
    city = models.CharField(default='nairobi', max_length=30)
    gender = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    return self.name
