from django.db import models

class Fruits(models.Model):
    COLOURS = (
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Green', 'Green'),
        ('Orange', 'Orange'),
    )
    SIZES = (
        ('Big', 'Big'),
        ('Medium', 'Medium'),
        ('Small', 'Small'),
    )

    name = models.CharField(max_length=200)
    colour = models.CharField(max_length=200, choices=COLOURS)
    size = models.CharField(max_length=200, choices=SIZES)

    def __str__(self):
        return self.name