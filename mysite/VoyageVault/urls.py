from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
#path('home/', views.homepage, name='home'),
    path('home/<int:user_profile_id>/', views.home, name='home'),
    path('place/<int:place_id>/', views.place_detail, name='place_detail'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('add-activity/<int:day_id>/', views.add_activity, name='add_activity'),
    path('day/<int:day_id>/', views.entry_detail, name='entry_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)