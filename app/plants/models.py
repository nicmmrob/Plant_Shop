from django.db import models

# Create your models here.
class Plants(models.Model):
    plant_id = models.AutoField(primary_key=True, serialize=True)
    care_guide = models.CharField(max_length=100, blank=True, default='')
    common_name = models.CharField(max_length=100, blank=True, null=True)
    sci_name = models.CharField(max_length=100, blank=False, default='')
    price = models.IntegerField(default=5)

 