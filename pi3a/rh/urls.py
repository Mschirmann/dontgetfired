from django.urls import path
from rh.views import (
    TimesheetListView,
    TimesheetRegisterView,
    AddUserView,
    UserProfileView,
    AdminVacationsView,
    AddVacationView,
    AdminHorasExtrasView,
    DashboardView,
)


app_name = "rh"
urlpatterns = [
    path("usuarios", AddUserView.as_view(), name="user_register"),
    path("ferias", AdminVacationsView.as_view(), name="ferias_form"),
    path("ferias/add", AddVacationView.as_view(), name="ferias_register"),
    path("horas_extras", AdminHorasExtrasView.as_view(), name="horas_extras"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path(
        "user/profile",
        UserProfileView.as_view(template_name="rh/user_profile.html"),
        name="user_profile",
    ),
    path("timesheet/list", TimesheetListView.as_view(), name="timesheet_list"),
    path(
        "timesheet/register", TimesheetRegisterView.as_view(), name="timesheet_register"
    ),
]
