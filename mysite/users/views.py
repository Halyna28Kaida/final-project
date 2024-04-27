from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import NewUserForm, LoginUserForm



class Register(CreateView):
    form_class = NewUserForm
    template_name = "users/register.html"
    success_url = '/myapp/home/'


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = '/myapp/home/'

    def get_success_url(self):
        return self.success_url
    

class Logout(LogoutView):
    login_url = 'myapp:home'
    next_page = '/myapp/home/'

