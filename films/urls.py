from django.urls import path
from films.views import IndexView, LoginView, RegisterView, check_username
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]

htmx_urlpatterns = [
    path("check_username/", check_username, name="check-username"),
]

urlpatterns += htmx_urlpatterns
