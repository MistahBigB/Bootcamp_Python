from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    muscle_group = models.CharField(max_length=50)
    ex_type = models.CharField(max_length=50)
    equipment = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    youtube = models.URLField()
    img = models.ImageField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'