from django.db import models
from django.contrib.auth.models import User


class AdventureClub(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    club_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11, default='')
    email = models.EmailField(null=True)
    featured = models.BooleanField(default=False)
    club_image = models.ImageField(upload_to='AdventureClub/Club_Images', null=True)
    club_address = models.CharField(max_length=80)
    city = models.CharField(null=False, blank=False, default="", max_length=25)

    def __str__(self):
        return self.club_name


class AdventureEvent(models.Model):
    # event_by = models.ForeignKey(AdventureClub, on_delete=models.CASCADE)
    event_by = models.CharField(max_length=50)
    title = models.CharField(max_length=80)
    overview = models.CharField(max_length=120, default='')
    image = models.ImageField(null=True, upload_to='AdventureClub/AdventureEventPics')
    featured = models.BooleanField(default=False)
    event_start_date = models.DateField()
    event_end_date = models.DateField()

    def __str__(self):
        return "Event- " + self.title


class EventDetails(models.Model):

    booked_event = models.ForeignKey(AdventureEvent, on_delete=models.CASCADE)
    start_point = models.CharField(max_length=70, null=True)
    destination = models.CharField(max_length=70, null=True)

    def __str__(self):
        return "BookedEventFrom- " + str(self.booked_event)


class TouristReview(models.Model):
    tourist_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    adventureevent = models.ForeignKey(AdventureEvent, on_delete=models.CASCADE)
    tourist_review = models.CharField(max_length=256)

    def __str__(self):
        return str(self.tourist_id)
