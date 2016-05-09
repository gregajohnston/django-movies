from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.order_by('-rel_date')[:5]
    context = {'latest_movie_list': latest_movie_list}
    return render(request, 'items/index.html',  context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'items/detail.html', {'movie': movie})


def rating(request, item_id):
    rating = "You're looking at the rating of movie %s."
    return HttpResponse(rating % item_id)
