from django.db import models

# Create your models here.
class paragr(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    time=models.DateTimeField()

    def __str__(self):
        return self.title
