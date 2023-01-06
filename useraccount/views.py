from django.contrib.auth.views import LoginView
from useraccount.forms import CustomRegisterForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "login.html"


class CustomRegisterView(CreateView):
    model = User
    form_class = CustomRegisterForm
    template_name = "register.html"