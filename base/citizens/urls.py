from django.urls import include, path
from . import views

app_name='citizens'
urlpatterns = [
    path("", views.index, name="index"),

]