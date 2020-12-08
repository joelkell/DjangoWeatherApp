from django.contrib.gis import admin
from .models import PreviousLocations


class PreviousLocationsAdmin(admin.GeoModelAdmin):
    fields = ['user', 'location', 'location_name']
    readonly_fields = ('created',)


admin.site.register(PreviousLocations, PreviousLocationsAdmin)
