from django.urls import path
from rh.views import (
    UserListView,
    UserDetailView,
    TimesheetListView,
    TimesheetRegisterView,
    NewUserView,
    NewUserHome
)


app_name = "rh"
urlpatterns = [
    path("user/register", NewUserView.as_view(), name="user_register"),
    path("home/admin", NewUserHome.as_view(), name="home_admin"),
    path("user/list", UserListView.as_view(), name="users"),
    path("user/form/<int:pk>", UserDetailView.as_view(), name="user_form"),
    path("timesheet/list", TimesheetListView.as_view(), name="timesheet_list"),
    path(
        "timesheet/register", TimesheetRegisterView.as_view(), name="timesheet_register"
    ),
]
