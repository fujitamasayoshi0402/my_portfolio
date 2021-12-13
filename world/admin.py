from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from world.models import Border, School, Facility, Busstop

admin.site.register(Border, admin.GeoModelAdmin)
admin.site.register(School, admin.GeoModelAdmin)
admin.site.register(Facility, admin.GeoModelAdmin)
admin.site.register(Busstop, admin.GeoModelAdmin)
