from django.views.generic import TemplateView, DetailView, ListView
from .models import User, Time_sheet, Holidays, Vacations


class UserRegisterView(TemplateView):
    model = User
    template_name = "rh/user_form.html"


class UserDetailView(DetailView):
    model = User
    template_name = "rh/user_detail.html"


class UserListView(ListView):
    model = User
    template_name = "rh/user_list.html"
    context_object_name = "user_list"


class TimesheetListView(ListView):
    model = Time_sheet
    template_name = "rh/timesheet_list.html"


class TimesheetRegisterView(TemplateView):
    model = Time_sheet
    template_name = "rh/timesheet_form.html"


class VacationListView(ListView):
    model = Vacations
    template_name = "rh/vacation_list.html"


class VacationRegisterView(TemplateView):
    model = Vacations
    template_name = "rh/vacation_form.html"


class HolidayListView(ListView):
    model = Holidays
    template_name = "rh/holiday_list.html"
