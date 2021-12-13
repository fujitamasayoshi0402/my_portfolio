from django.contrib.gis.db import models

# Create your models here.


class Border(models.Model):
    n03_001 = models.CharField(max_length=10)
    n03_002 = models.CharField(max_length=20)
    n03_003 = models.CharField(max_length=20)
    n03_004 = models.CharField(max_length=20)
    n03_007 = models.CharField(max_length=5)
    geom = models.PolygonField(srid=6668)
