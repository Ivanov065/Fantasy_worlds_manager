from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Введите ваш юзернейм", "class":"form-control mb-3"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Придумайте пароль", "class":"form-control mb-3"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль", "class":"form-control mb-3"})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Введите ваш юзернейм", "class":"form-control mb-3"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль", "class":"form-control mb-3"})
    )

    class Meta:
        model = User
        fields = ["username", "password"]
