from django.views import generic
from .models import User, Time_sheet, Holidays, Vacations


class HomeView(generic.TemplateView):
    template_name = "rh/home.html"


class LoginView(generic.TemplateView):
    template_name = "rh/login.html"


class UserRegisterView(generic.TemplateView):
    model = User
    template_name = "rh/user_form.html"


class UserDetailView(generic.DetailView):
    model = User
    template_name = "rh/user_detail.html"


class UserListView(generic.ListView):
    model = User
    template_name = "rh/user_list.html"
    context_object_name = "user_list"


class TimesheetListView(generic.ListView):
    model = Time_sheet
    template_name = "rh/timesheet_list.html"


class TimesheetRegisterView(generic.TemplateView):
    model = Time_sheet
    template_name = "rh/timesheet_form.html"


class VacationListView(generic.ListView):
    model = Vacations
    template_name = "rh/vacation_list.html"


class VacationRegisterView(generic.TemplateView):
    model = Vacations
    template_name = "rh/vacation_form.html"


class HolidayListView(generic.ListView):
    model = Holidays
    template_name = "rh/holiday_list.html"
