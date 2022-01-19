from django.urls import path
from app_media.views import *


urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    # path('check_file/', check_file, name='check_file'),


]