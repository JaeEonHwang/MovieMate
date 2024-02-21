import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import requests

from movies.models import People, Roles, Movies, Credits, Genres, ImageTypes, ImagePaths, Videos, Keywords

# # now_playing 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/now_playing?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['results']
# for movie in movies:
#     Movies.objects.update_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title'], 'now_playing': True})

# # top_ rated 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/top_rated?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['results']
# for movie in movies:
#     Movies.objects.update_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title'], 'top_rated': True})
    



# # upcoming 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/upcoming?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['results']
# for movie in movies:
#     # print(movie)
#     a = Movies.objects.update_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title'], 'upcoming': True})


# related_movie 데이터 추가
movies = Movies.objects.all()
for i in range(21067, 62165):
    movie = Movies.objects.get(pk=i)
    id = movie.tmdb_id
    url = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=e95b79709ef9e216e667b4d9554f60f5'
    response = requests.get(url)
    data = response.json()
    results = data.get('results', [])
    for result in results:
        # a = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
        a = Movies.objects.get_or_create(tmdb_id=result['id'], defaults={'adult': result['adult'], 'overview': result['overview'], 'popularity': result['popularity'], 'release_date': result['release_date'], 'title': result['title']})
        movie.related_movie.add(a[0])