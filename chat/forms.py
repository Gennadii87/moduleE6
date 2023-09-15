from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Форма для регистрации пользователя
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User  # Используем стандартную модель пользователя Django
        fields = ['username', 'email', 'password1', 'password2']