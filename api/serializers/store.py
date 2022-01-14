from rest_framework.serializers import ModelSerializer

from api.models import Box


class StaffBoxSerializer(ModelSerializer):
    class Meta:
        model = Box
        fields = "__all__"


class BoxSerializer(StaffBoxSerializer):
    class Meta:
        model = Box
        exclude = ("created_by", "last_updated", "created_on")
