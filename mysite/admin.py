from django.contrib import admin
from .models import OwnershipInfo, IdentifiedNew, Shamba,MonthlyWeatherByCity
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class ShambaAdmin(LeafletGeoAdmin):
	fields = ('balance','objectid_1','objectid','shape_leng','perimeter','parcel_no','shamba_owner','soil_type','state','cost_value','pic_url','electricit','water','outlinetra',
		'shape_le_1','shape_area','geom')
	list_display = ['balance','objectid_1','objectid','shape_leng','perimeter','parcel_no','shamba_owner','soil_type','state','cost_value','pic_url','electricit','water']
	class Meta:
		ordering = ('balance',)

admin.site.register(Shamba,ShambaAdmin)

@admin.register(OwnershipInfo)
class OwnershipInfoAdmin(LeafletGeoAdmin):
    list_display = ('first_name', 'id_number')


@admin.register(IdentifiedNew)
class IdentifiedNewAdmin(LeafletGeoAdmin):
    list_display = ['name']


@admin.register(MonthlyWeatherByCity)
class MonthlyWeatherByCityAdmin(LeafletGeoAdmin):
    list_display = ('month', 'boston_temp')