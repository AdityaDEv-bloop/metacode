from django.urls import path
from . import views


urlpatterns = [
    path("",views.index.index, name="index"),
    path("about/",views.about.about, name="about"),
]