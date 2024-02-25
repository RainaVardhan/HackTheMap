# from django.contrib import admin
from django.urls import path, include
# from django.views.generic import RedirectView

urlpatterns = [
    #re_path(r'^$', RedirectView.as_view(url='/VoyageVault/login/', permanent=True)),
    path("VoyageVault/", include("VoyageVault.urls")),
    # path("admin/", admin.site.urls),
    # path("", include("VoyageVault.urls"))
]