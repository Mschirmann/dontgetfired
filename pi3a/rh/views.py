from collections import defaultdict
import datetime
import calendar
from functools import reduce
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView
from .forms import UserForm, VacationForm, TimesheetForm
from .models import User, Time_sheet, Holidays, Vacations
from django.http import JsonResponse
from django.db.models import F, Sum, DateField, CharField, Value, Func
from django.db.models.functions import (
    Trunc,
    TruncDay,
    ExtractDay,
    ExtractMonth,
    Concat,
)
from django.utils.timezone import localtime
import pytz


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
    template_name = "rh/horas_extras.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        # get request params
        user_id = int(kwargs["user_id"])
        month = kwargs["month"]
        input_dt = month.split("-")

        # get month last day do filter query
        period = calendar.monthrange(int(input_dt[0]), int(input_dt[1]))
        start_date = input_dt[0] + "-" + input_dt[1] + "-01"
        end_date = input_dt[0] + "-" + input_dt[1] + "-" + str(period[1])

        # query using date range and user
        times_query = Time_sheet.objects.filter(
            fk_user_id=user_id, created_at__range=[start_date, end_date]
        ).order_by("created_at")

        # variables used inside loop to format chart
        tz = pytz.timezone("America/Sao_Paulo")
        prev_date = None
        datasets = []
        extra_hours = 0
        for times in times_query:
            full_date = localtime(times.created_at, tz)
            if not prev_date:
                prev_date = full_date

            if prev_date.day == full_date.day:
                diff = full_date - prev_date
                datasets.append(
                    {
                        "day": datetime.datetime.strftime(full_date, "%d/%m"),
                        "hours_worked": diff.seconds,
                    }
                )
                prev_date = full_date
            else:
                prev_date = None

        dataset_values = defaultdict(int)
        for item in datasets:
            day = item["day"]
            seconds = item["hours_worked"]
            dataset_values[day] += seconds // 3600
            if dataset_values[day] > 8:
                extra_hours = extra_hours + (dataset_values[day] - 8)
        data = {
            "labels": list(dataset_values.keys()),
            "datasets": [
                {
                    "label": "Horas trabalhadas",
                    "backgroundColor": "#28734e",
                    "borderColor": "#28734e",
                    "data": list(dataset_values.values()),
                }
            ],
            "extra_hours": extra_hours,
        }

        return JsonResponse({"data": data})


class TimesheetListView(ListView):
    template_name = "rh/timesheet_list.html"
    context_object_name = "timesheet_list"

    def get_queryset(self):
        queryset = Time_sheet.objects.all()
        if self.request.user.is_authenticated:
            Time_sheet.objects.filter(fk_user=self.request.user)
        return queryset
