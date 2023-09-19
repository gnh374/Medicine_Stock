from django.db import models

#model dengan atribut name, amount, dan description
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    