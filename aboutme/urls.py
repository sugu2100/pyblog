from django.urls import path

from aboutme import views

app_name = "aboutme"

urlpatterns = [
    path('', views.profile, name='profile')
]