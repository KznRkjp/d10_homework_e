from django.contrib import admin
from carlist.models import Car, Modeltype, Manufacturer, Productionyear
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
    # list_display = ('manufacturer','model','production_year', 'gearbox_type', 'color')
    # search_fields = ['manufacturer', 'model', 'production_year', 'color']
    #
    # def get_ordering(self, request):
    #     return ['manufacturer']
    # pass
@admin.register(Modeltype)
class ModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Productionyear)
class ProductionyearAdmin(admin.ModelAdmin):
    pass
