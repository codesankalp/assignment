from django_filters import FilterSet

from api.models import Box


class BoxFilter(FilterSet):

    class Meta:
        model = Box
        fields = {
            "length": ["lt", "gt"],
            "width": ["lt", "gt"],
            "height": ["lt", "gt"],
            "area": ["lt", "gt"],
            "volume": ["lt", "gt"],
            "created_by__username": ["exact"],
            "created_on": ["lt", "gt"],
        }
