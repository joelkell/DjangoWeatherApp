from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class PreviousLocations(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=True)
    location = models.PointField(
        editable=True,
        blank=True,
        null=True,
        default=None, )
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        ordering = ['-created']
