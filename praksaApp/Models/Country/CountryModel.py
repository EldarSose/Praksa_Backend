from django.db import models

class Country(models.Model):
    countryId = models.IntegerField(primary_key = True)
    countryName = models.CharField(max_length=200)
    
    class Meta:
        db_table = "Country"