from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self , object): #elobjeto contiene los datos de neustro modelo
        return format_html( '<img src="{}"  width="40" style="border-radius:50px"/>'.format(object.photo.url))
    
    thumbnail.short_description = 'PHOTO'
    
    list_display = ('id','thumbnail','firstname','designation','created_date')#tupla
    list_display_links = ('id','firstname','thumbnail')
    search_fields = ('firstname','lastname','designation')
    list_filter = ('firstname','lastname','designation')




admin.site.register(Team,TeamAdmin)
