from django.db import models

# Create your models here.

# Measure represent de model of data we want to save from CSV file to DB  
class Measure(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField('timestamp')
    energy = models.DecimalField(max_digits=7, decimal_places=3)
    reactiveEnergy = models.DecimalField(max_digits=7, decimal_places=3)
    power = models.DecimalField(max_digits=7, decimal_places=3)
    maximeter = models.DecimalField(max_digits=7, decimal_places=3) 
    reactivePower = models.DecimalField(max_digits=7, decimal_places=3)
    voltage = models.DecimalField(max_digits=7, decimal_places=3)
    intensity = models.DecimalField(max_digits=7, decimal_places=3)
    powerFactor = models.DecimalField(max_digits=7, decimal_places=3)
    
    def __str__(self):
        return str(self.id)

