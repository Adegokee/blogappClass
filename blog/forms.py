from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    class Meta:
        models=Room
        field="__all__"