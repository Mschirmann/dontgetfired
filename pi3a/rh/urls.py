from django.urls import path
from rh.views import (
    UserListView,
    UserDetailView,
    TimesheetListView,
    TimesheetRegisterView,
    NewUserView,
    UserProfileView,
    AdminVocationsView,
    AdminHorasExtrasView
)


app_name = "rh"
urlpatterns = [
    path("user/register", NewUserView.as_view(), name="user_register"),
    path("ferias", AdminVocationsView.as_view(), name="ferias"),
    path("horas_extras", AdminHorasExtrasView.as_view(), name="horas_extras"),
    path(
        "user/profile",
        UserProfileView.as_view(template_name="rh/user_profile.html"),
        name="user_profile",
    ),
    path("user/list", UserListView.as_view(), name="users"),
    path("user/form/<int:pk>", UserDetailView.as_view(), name="user_form"),
    path("timesheet/list", TimesheetListView.as_view(), name="timesheet_list"),
    path(
        "timesheet/register", TimesheetRegisterView.as_view(), name="timesheet_register"
    ),
]
