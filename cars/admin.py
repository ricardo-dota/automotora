from django.contrib import admin
from .models import Cars
from django.utils.html import format_html


# Register your models here.

class CardAdmin(admin.ModelAdmin):
    
    def thumbnail(self , object): #elobjeto contiene los datos de neustro modelo
        return format_html( '<img src="{}"  width="40""/>'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Imagen'

    list_display        = ( 'car_title','thumbnail' ,'color', 'model', 'year', 'body_Style', 'fuel_type','is_featured' )
    list_display_links  = ( 'car_title','thumbnail')
    search_fields       =  ( 'car_title''model', 'year')
    list_editable       = ('is_featured', )
    list_filter         = ( 'model',  'fuel_type'  ,'color')



admin.site.register(Cars,CardAdmin)
