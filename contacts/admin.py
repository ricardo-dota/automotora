from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display        = ('id','first_name','last_name','city','email','car_title','create_date')
    list_display_links  = ( 'id','first_name','last_name','email')
    list_per_page       = 25



admin.site.register(Contact,ContactAdmin)