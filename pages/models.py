from django.db import models

# Create your models here.

class Team(models.Model):
    photo               =  models.ImageField( upload_to = 'photos/%Y/%m/%d')
    firstname           =  models.CharField( max_length=255)
    lastname            =  models.CharField( max_length=255)
    designation         =  models.CharField( max_length=255)
    facebook_link       =  models.URLField( max_length=100)
    twittter_link       =  models.URLField( max_length=100)
    google_plust_link   =  models.URLField( max_length=100)
    created_date        =  models.DateField( auto_now_add = True)

    def __str__(self):
        return self.firstname