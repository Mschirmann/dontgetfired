import datetime
from django.views.generic import TemplateView, DetailView, ListView, View
from .models import User, Time_sheet, Holidays, Vacations
from django.http import HttpResponse


class UserProfileView(TemplateView):
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vacations"] = self.get_user_vacation()
        context["last_registers"] = self.get_recently_user_timesheet()
        context["holiday"] = self.get_holiday()
        return context

    def get_user_vacation(self):
        if self.request.user.is_authenticated:
            # get last vacation register
            vacation = (
                Vacations.objects.filter(fk_user=self.request.user, confirmed=True)
                .order_by("-id")
                .last()
            )
            return vacation
        return None

    def get_recently_user_timesheet(self):
        if self.request.user.is_authenticated:
            # get last 5 timesheet register
            last_registers = Time_sheet.objects.filter(
                fk_user=self.request.user
            ).order_by("-created_at")[:5][::-1]
            return last_registers
        return None

    def get_holiday(self):
        today = datetime.datetime.today()
        current_year = today.year
        current_month = today.month
        current_day = today.day

        holidays = Holidays.objects.filter(
            year=current_year, month=current_month, day=current_day
        )

        if holidays.exists():
            return holidays.last()
        return None


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
    template_name = "rh/timesheet_list.html"
    context_object_name = "timesheet_list"

    def get_queryset(self):
        queryset = Time_sheet.objects.all()
        if self.request.user.is_authenticated:
            Time_sheet.objects.filter(fk_user=self.request.user)
        return queryset


class TimesheetRegisterView(View):
    def post(self, request, *args, **kwargs):
        print(request.user)
        print(request.POST["register"])
        Time_sheet.objects.create(fk_user=request.user)

        return HttpResponse(True, status=201)


class VacationListView(ListView):
    model = Vacations
    template_name = "rh/vacation_list.html"


class VacationRegisterView(TemplateView):
    model = Vacations
    template_name = "rh/vacation_form.html"


class HolidayListView(ListView):
    model = Holidays
    template_name = "rh/holiday_list.html"
