from django.contrib import admin
from . import models

admin.site.register(models.AdventureClub)
admin.site.register(models.AdventureEvent)
admin.site.register(models.EventDetails)
admin.site.register(models.TouristReview)
