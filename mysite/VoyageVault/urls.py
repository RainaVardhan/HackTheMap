from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    #path('', views.home, name='home'),
    path('travel-places/', views.travel_places, name='travel_places'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
]