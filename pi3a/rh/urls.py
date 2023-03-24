from django.urls import path
from rh.views import UserListView, UserDetailView, TimesheetListView, UserRegisterView1, UserHomeView


app_name = "rh"
urlpatterns = [
    path("user/list", UserListView.as_view(), name="users"),
    path("user/home", UserHomeView.as_view(), name="home"),
    path("user/register", UserRegisterView1.as_view(), name="register"),
    path("user/detail/<int:pk>", UserDetailView.as_view(), name="user_detail"),
    path("timesheet/list", TimesheetListView.as_view(), name="timesheet_list"),
]
