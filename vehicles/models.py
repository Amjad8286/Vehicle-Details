from django.db import models

# Create your models here.
class VehiclesDetail(models.Model):
    v_id = models.AutoField(primary_key=True)
    engine_status = models.CharField(max_length=200)
    fuel_level = models.CharField(max_length=200)
    tampreture = models.CharField(max_length=200)
    average_speed = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)

    def __str__(self):
        return self.engine_status + " " + self.speed
        