from django.db import models
from django.contrib.auth.models import User

#model dengan atribut name, amount, dan description
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

