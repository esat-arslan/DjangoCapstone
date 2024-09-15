from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class InputForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    message = models.CharField(max_length=100)
    roll_number = models.IntegerField(
        validators=[MaxValueValidator(999999)]
    )
    password = models.CharField(max_length=100)