from django import forms

from .models import Squirrel


class SquirrelForm(forms.ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'
