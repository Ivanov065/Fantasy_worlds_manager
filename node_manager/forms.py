from django import forms
from .models import Nodes, AccessModes, NodePiece

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

class NodePieceForm(forms.ModelForm):

    piece_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control piece_name_input", "id": "piece_name_input"})
    )

    is_secret = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class":"form-check-input mx-2 is_secret_input", "id":"is_secret_input"}),
        required=False
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control body_input", "id": "body_input"})
    )

    class Meta:
        model = NodePiece
        fields = ["piece_name", "is_secret", "body"]

