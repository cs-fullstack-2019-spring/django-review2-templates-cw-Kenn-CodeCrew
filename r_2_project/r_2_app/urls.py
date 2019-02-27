from django.urls import path

# import endpoints_app
from . import views

urlpatterns = [
    path('songs/', views.list_songs, name='list_songs'),
    # path('songs/<int:song_id>/', views.song_details, name='songs'),
    path('details/<int:song_id>/', views.song_details, name='song_details'),
    path('superdetails/<int:song_id>/', views.song_superdetails, name='song_superdetails'),
    ]

