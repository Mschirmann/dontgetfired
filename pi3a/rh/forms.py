from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vacations, Time_sheet


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class VacationForm(ModelForm):
    class Meta:
        model = Vacations
        fields = "__all__"


class TimesheetForm(ModelForm):
    class Meta:
        model = Time_sheet
        fields = ["fk_user"]
