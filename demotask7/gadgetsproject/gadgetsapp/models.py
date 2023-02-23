from django.db import models

# Create your models here.
class Gadgets(models.Model):
    title=models.CharField(max_length=250)
    desc=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title
