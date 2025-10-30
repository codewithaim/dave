from django.db import models

# Create your models here.
class Data(models.Model):
    property_name = models.CharField(max_length=200)
    property_price = models.FloatField()
    property_rent = models.FloatField()
    emi = models.FloatField()
    tax = models.FloatField()
    other_exp = models.FloatField()
    monthly_expenses = models.FloatField(default=0)
    monthly_income = models.FloatField(default=0)
