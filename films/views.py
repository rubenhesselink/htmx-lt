from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth import get_user_model

from films.forms import RegisterForm
from films.models import Movie


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(DjangoLoginView):
    template_name = "registration/login.html"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MovieOverviewView(ListView):
    model = Movie
    template_name = "movie-overview.html"
    context_object_name = "movies"


class MyMovieListView(ListView):
    model = Movie
    template_name = "my-movie-list.html"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_username = self.request.user.username
        context["movie_option_list"] = Movie.objects.exclude(users_with_movie_in_list__username=user_username)
        return context

    def get_queryset(self):
        user_username = self.request.user.username
        return Movie.objects.filter(users_with_movie_in_list__username=user_username)


def check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<div id='username-error' class='error'>This username already exists</div>")
    return HttpResponse("<div id='username-error' class='success'>This username is available</div>")


def add_movie(request):
    movie_title = request.POST.get("moviename")
    Movie.objects.get_or_create(title=movie_title)

    movies = Movie.objects.all()
    return render(request, "partials/movie-list.html", {"movies": movies})


def add_movie_to_my_list(request):
    movie_title = request.POST.get("movie-select-box")
    movie = Movie.objects.get(title=movie_title)
    movie.users_with_movie_in_list.add(request.user)
    user_username = request.user.username
    movies = Movie.objects.filter(users_with_movie_in_list__username=user_username)
    return render(request, "partials/movie-list.html", {"movies": movies})
