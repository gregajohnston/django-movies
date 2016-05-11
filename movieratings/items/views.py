from django.shortcuts import render, get_object_or_404
from .models import Movie, Rating
# from django.views.generic.list import ListView


# class MovieList(ListView):
#     model = Movie
#     context_object_name = 'movies'


def movie_list(request):
    alphabet_movie_list = Movie.objects.order_by('title')
    context = {'alphabet_movie_list': alphabet_movie_list}
    return render(request, 'items/movie_list.html',  context)


def detail(request, mov_id):
    movie = get_object_or_404(Movie, pk=mov_id)
    context = {'movie': movie}
    return render(request, 'items/detail.html', context)


def rating(request, mov_id):
    rate = get_object_or_404(Rating, pk=mov_id)
    context = {'rating': rate}
    return render(request, 'items/rate.html', context)
