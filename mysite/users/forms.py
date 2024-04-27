from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import TuristUserNew


class NewUserForm(UserCreationForm):
    class Meta:
        model = TuristUserNew  
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    email = forms.CharField(label="E-mail", widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Проверка пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class LoginUserForm(AuthenticationForm):  
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    # class Meta:
    #     model = TuristUserNew
    #     fields = ['email', 'username', 'first_name','last_name', 'password1', 'password2']
    #     label = {
    #         'email': 'E-mail',
    #         'username': 'Имя пользователя',
    #         'first_name': 'Имя',
    #         'last_name': 'Фамилия',
            
    #     }

    #     widgets = {
    #         'email': forms.TextInput(attrs={'class': 'form-input'}),
    #         'first_name': forms.TextInput(attrs={'class': 'form-input'}),
    #         'last_name': forms.TextInput(attrs={'class': 'form-input'}),
    #     }
        