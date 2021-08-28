from django.db import models

# Create your models here.
class demo_v1(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='try_pics')
    des = models.TextField()

    def __str__(self):
        return self.name