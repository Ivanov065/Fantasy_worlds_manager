from django import forms
from .models import Nodes, AccessModes

class NodeTreeForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Имя вашего дерева", "id" : "name_input"})
    )
    access_mode = forms.ModelChoiceField(
        queryset=AccessModes.objects.all(),
        to_field_name="name",
        widget=forms.Select(attrs={"class": "form-control", "id" : "access_mode_input"}),
        empty_label='(nothing)'
    )
    
    class Meta:
        model = Nodes
        fields = ["name", "access_mode"]
