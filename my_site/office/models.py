from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Patient(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(50)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(0)])

    def __str__(self):
        return f'Nama saya adalah {self.first_name} dan nama belakang saya {self.last_name} umur saya {self.age}'
# Create your models here.
