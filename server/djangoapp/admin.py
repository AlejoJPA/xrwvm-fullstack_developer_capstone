"""Admin configuration for Django models."""


from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    '''InLine for CarModel in CarMake admin'''
    model = CarModel
    extra = 1


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    '''Admin configuration for CarModel'''
    list_display = ('name', 'car_make', 'car_type', 'year')
    list_filter = ('car_type', 'year', 'car_make')
    search_fields = ('name',)


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    '''Admin configuration for CarMake'''
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
