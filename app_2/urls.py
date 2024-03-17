from django.urls import path
from . import views

urlpatterns = [
path('/p/', views.post, name='Psy_home'),
path('/p/profile', views.post, name='Psy_profile'),
path('/p/schedule', views.post, name='Psy_schedule'),
path('/p/earning', views.post, name='Psy_earning'),

]