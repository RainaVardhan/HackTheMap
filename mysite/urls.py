# from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("VoyageVault/", include("VoyageVault.urls")),
    # path("admin/", admin.site.urls),
    # path("", include("VoyageVault.urls"))
]