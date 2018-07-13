from django import forms
from winetasting.models import WineTastingInfo
from django.contrib.auth.models import User


class WineTastingInfoForm(forms.ModelForm):

    class Meta():
        model = WineTastingInfo
        fields = '__all__'
