from django.urls import path,include,re_path
from .views import TeamViewSet
from rest_framework.routers import DefaultRouter
from . import views

#
router = DefaultRouter()
router.register("team", TeamViewSet, basename="team")




urlpatterns = [
    re_path('', include(router.urls)),
    path("send", views.mail_index,name="mail_index")

]