from django.urls import path
from . import views

urlpatterns = [
path('p', views.p_post, name='Psy_home'),
path('p/profile', views.p_schedule, name='Psy_profile'),
path('p/schedule', views.p_schedule, name='Psy_schedule'),
path('p/earning', views.p_earning, name='Psy_earning'),
path('p/earning', views.p_profile, name='Psy_earning'),

]