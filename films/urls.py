from django.urls import path
from films.views import IndexView, LoginView, RegisterView, MovieOverviewView, MyMovieListView, check_username, add_movie_to_my_list, add_movie
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("movies/", MovieOverviewView.as_view(), name="movie-overview"),
    path("movies/my-list/", MyMovieListView.as_view(), name="my-movie-list"),
]

htmx_urlpatterns = [
    path("check_username/", check_username, name="check-username"),
    path("add-movie/", add_movie, name="add-movie"),
    path("add-movie-to-my-list/", add_movie_to_my_list, name="add-movie-to-my-list"),
]

urlpatterns += htmx_urlpatterns
