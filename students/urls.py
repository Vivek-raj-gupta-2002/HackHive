from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='student_post'),
    path('psyco', views.helpers, name='psyco'),
    path('community', views.community, name='community'),
    path('dash', views.dash, name='dash'),
]