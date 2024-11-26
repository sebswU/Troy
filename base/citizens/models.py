from django.db import models

# Create your models here.

class Person(models.Model):
    """
    Each accepted person gets a Person object:
    Name - Name of person
    id - primary key, goes 00 up to 99
    added - time registered in DateTimeField form
    """
    name = models.CharField(max_length=100)
    id = models.DecimalField(decimal_places=0, max_digits=2, primary_key=True)
    added = models.DateTimeField("Date/Time Added")

    def __str__(self) -> str:
        return self.name