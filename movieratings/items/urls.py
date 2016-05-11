from django.conf.urls import url

from . import views

app_name = 'items'

urlpatterns = [
    url(r'^movies/$', views.movie_list, name='movie_list'),
    url(r'^movies/(?P<mov_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^movies/(?P<mov_id>[0-9]+)/rating/$', views.rating, name='rating'),
]
