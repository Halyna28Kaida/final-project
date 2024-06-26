from django.urls import path
from users.views import Login, Logout, Register


app_name= 'users'

urlpatterns = [
    path('register/', Register.as_view(), name='register' ),
    path('login/', Login.as_view(), name='login' ),
    path('logout/', Logout.as_view(), name='logout' ),
]

