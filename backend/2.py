import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import requests

from movies.models import People, Roles, Movies, Credits, Genres, ImageTypes, ImagePaths, Videos, Keywords


# 키워드 데이터 넣기
for i in range(35908, 62165):
    movie = Movies.objects.get(pk=i)
    id = movie.tmdb_id
    url = f'https://api.themoviedb.org/3/movie/{id}/keywords?api_key=e95b79709ef9e216e667b4d9554f60f5'
    response = requests.get(url)
    data = response.json()
    keywords = data.get('keywords', [])
    for keyword in keywords:
        a = Keywords.objects.get_or_create(tmdb_id=keyword['id'], defaults={'name': keyword['name']})
        a[0].movies.add(movie)


