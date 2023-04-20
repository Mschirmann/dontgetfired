import datetime
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from .forms import UserForm, VacationForm, TimesheetForm
from .models import User, Time_sheet, Holidays, Vacations


class UserProfileView(TemplateView):
    context_object_name = "user_profile"
    template_name = "rh/user_profile.html"

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


class AddUserView(CreateView):
    form_class = UserForm
    template_name = "rh/user_register.html"
    success_url = "rh/usuarios/"


class AdminVacationsView(TemplateView):
    template_name = "rh/ferias.html"
    model = Vacations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class AddVacationView(CreateView):
    form_class = VacationForm
    success_url = "/rh/ferias"
    template_name = "rh/ferias.html"


class TimesheetRegisterView(CreateView):
    form_class = TimesheetForm
    success_url = "/rh/user/profile"
    template_name = "rh/timesheet_list.html"

    def form_valid(self, form):
        last_register = (
            Time_sheet.objects.filter(fk_user=self.request.user).order_by("id").last()
        )
        if last_register is None or last_register.type == "Saída":
            type = "Entrada"
        else:
            type = "Saída"
        form.instance.type = type
        return super().form_valid(form)


class AdminHorasExtrasView(TemplateView):
    model = User
    template_name = "rh/horas_extras.html"


class DashboardView(View):
    def get(self, request):
        return "to do"


class TimesheetListView(ListView):
    template_name = "rh/timesheet_list.html"
    context_object_name = "timesheet_list"

    def get_queryset(self):
        queryset = Time_sheet.objects.all()
        if self.request.user.is_authenticated:
            Time_sheet.objects.filter(fk_user=self.request.user)
        return queryset
