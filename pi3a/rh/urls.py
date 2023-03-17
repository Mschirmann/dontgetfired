from django.urls import path

from rh.views import HomeView, LoginView, UserListView, UserDetailView


app_name = "rh"
urlpatterns = [
    # used to home page
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("user/list", UserListView.as_view(), name="users"),
    path("user/detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
]
