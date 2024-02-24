from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
#path('home/', views.homepage, name='home'),
    path('home/', views.home, name='home'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
]