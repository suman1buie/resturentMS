from django.db import models


class Tables(models.Model):
    location = models.CharField(max_length=30, null=True, blank=True)
    size = models.CharField(max_length=2, null=True, blank=True)
    totalTime = models.CharField(max_length=2, null=True, blank=True)
    started_timing = models.DateTimeField(null=True, blank=True)
    # price =
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.location
