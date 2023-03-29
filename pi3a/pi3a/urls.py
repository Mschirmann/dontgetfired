from django.contrib import admin
from django.urls import include, path
from rh.views import UserHomeView

urlpatterns = [
    path("", UserHomeView.as_view(), name="home"),
    path("rh/", include("rh.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
]
