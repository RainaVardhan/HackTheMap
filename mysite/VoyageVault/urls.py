from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('home/<int:user_profile_id>/', views.home, name='home'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('add_place/', views.add_place, name='add_place'),
    path('places/<int:place_id>/add_entry/', views.add_entry, name='add_entry'),
    path('places/<int:place_id>/delete/', views.delete_place, name='delete_place'),
    path('entries/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup, name='signup'),
]