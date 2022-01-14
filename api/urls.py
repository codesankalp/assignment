from django.urls import path
from django.urls.base import translate_url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import BoxViewSet

router = DefaultRouter(trailing_slash=False)
router.register("box", BoxViewSet)

urlpatterns = [path("token/", obtain_auth_token, name="")]
urlpatterns += router.urls
