from django.db import models

class medic(models.Model):
    Mname = models.CharField(max_length=100)
    Mdesc = models.TextField(max_length = 1200)
    Mstock = models.PositiveIntegerField(default=0)
    Mprice = models.DecimalField(max_digits = 10, decimal_places = 2)
