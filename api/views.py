from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.decorators import action
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.filters import BoxFilter
from api.models import Box
from api.permissions import BoxPermission
from api.serializers import BoxSerializer, StaffBoxSerializer


class BoxViewSet(ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    ]
    permission_classes = [BoxPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoxFilter

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffBoxSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(url_path="my-boxes", detail=False, methods=["GET"], name="Get My Boxes")
    def list_my_boxes(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise NotAuthenticated
        queryset = self.filter_queryset(self.get_queryset()).filter(
            created_by=request.user
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
