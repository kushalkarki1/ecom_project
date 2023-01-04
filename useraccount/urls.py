from django.urls import path
from useraccount.views import CustomLoginView

app_name = "user"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
]