from django.db import models

# Create your models here.


class House(models.Model):
    """Model Definition for Houses"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="per night")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, verbose_name="Pets Allowed?", help_text="Does the pets allowed?")
