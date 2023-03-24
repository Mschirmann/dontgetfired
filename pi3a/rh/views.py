from django.views.generic import TemplateView, DetailView, ListView
from .models import User, Time_sheet, Holidays, Vacations


class UserRegisterView(TemplateView):
    model = User
    template_name = "rh/user_form.html"

class UserRegisterView1(TemplateView):
    model = User
    template_name = "rh/user_register.html"

class UserHomeView(TemplateView):
    model = User
    template_name = "rh/user_home.html"

class UserDetailView(DetailView):
    model = User
    template_name = "rh/user_detail.html"


class UserListView(ListView):
    model = User
    template_name = "rh/user_list.html"
    context_object_name = "user_list"


class TimesheetListView(ListView):
    template_name = "rh/timesheet_list.html"
    context_object_name = "timesheet_list"

    def get_queryset(self):
        queryset = Time_sheet.objects.all()
        if self.request.user.is_authenticated:
            Time_sheet.objects.filter(fk_user=self.request.user)
        return queryset


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
