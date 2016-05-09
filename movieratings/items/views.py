from django.shortcuts import render, get_object_or_404
from .models import Movie, Rating


def index(request):
    latest_movie_list = Movie.objects.order_by('-rel_date')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'items/index.html',  context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'items/detail.html', {'movie': movie})


def rating(request, movie_id):
    rate = get_object_or_404(Rating, pk=movie_id)
    return render(request, 'items/rate.html', {'rating': rate})
