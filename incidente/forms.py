from django import forms
from .models import Incidente

class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = '__all__'
        exclude = ('fecha_modificacion',)

