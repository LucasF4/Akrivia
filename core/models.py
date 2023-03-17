from django.db import models

# Create your models here.

class Survivor(models.Model):

    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, default='')
    user_age = models.IntegerField(default=0)
    user_sex = models.CharField(max_length=1, default='')
    user_last_location = models.CharField(max_length=255, default='')

    def __str__(self):
        return f'Nome: {self.user_name}'

