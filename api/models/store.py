from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import gettext as _

from api.exceptions import (
    TotalAvgAreaException,
    TotalAvgUserVolException,
    TotalWeekBoxException,
    TotalWeekUserBoxException,
)

User = get_user_model()


class Box(models.Model):
    length = models.FloatField(help_text=_("Length of the box"))
    width = models.FloatField(help_text=_("Breadth of the box"))
    height = models.FloatField(help_text=_("Height of the box"))
    area = models.FloatField(help_text=_("Area of the box"), editable=False)
    volume = models.FloatField(help_text=_("Volume of the box"), editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Box - ({self.length}*{self.width}*{self.height})"

    def get_area(self):
        return 2 * (
            self.length * self.width
            + self.width * self.height
            + self.height * self.length
        )

    def get_volume(self):
        return self.length * self.width * self.height

    def get_area_sum(self, queryset):
        area = queryset.aggregate(Sum("area")).get("area__sum")
        return area if area else 0

    def get_vol_sum(self, queryset):
        vol = queryset.aggregate(Sum("volume")).get("volume__sum")
        return vol if vol else 0

    def get_week_box(self, queryset):
        return queryset.filter(
            created_on__gte=timezone.now() - timedelta(days=7)
        ).count()

    def save(self, *args, **kwargs):
        self.area = self.get_area()
        self.volume = self.get_volume()
        boxes = Box.objects.all()
        if self.pk:
            # update
            boxes = boxes.exclude(pk=self.pk)

        if (self.area + self.get_area_sum(boxes)) / (boxes.count() + 1) > settings.A1:
            raise TotalAvgAreaException

        if self.get_week_box(boxes) + 1 > settings.L1:
            raise TotalWeekBoxException

        user_boxes = boxes.filter(created_by=self.created_by)

        if self.get_week_box(user_boxes) + 1 > settings.L2:
            raise TotalWeekUserBoxException

        if (self.volume + self.get_vol_sum(user_boxes)) / (
            user_boxes.count() + 1
        ) > settings.V1:
            raise TotalAvgUserVolException

        super(Box, self).save(*args, **kwargs)
