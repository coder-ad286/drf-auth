from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20,null=False)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=False)
    description = models.TextField(null=False)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
   
