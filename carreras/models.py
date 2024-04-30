from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Carreras(models.Model):
    title = models.CharField(max_length=100)
    imge = ImageField(upload_to='carreras/images')