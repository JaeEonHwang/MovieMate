import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import requests
from django.conf import settings
from movies.models import People, Roles, Movies, Credits, Genres, ImageTypes, ImagePaths, Videos, Keywords, Profile
from accounts.models import User


# video 데이터 넣기
# movies = Movies.objects.all()
# for i in range(38658, 62165):
#     movie = Movies.objects.get(pk=i)
#     id = movie.tmdb_id
#     url = f'https://api.themoviedb.org/3/movie/{id}/videos?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(url)
#     data = response.json()
#     videos = data.get('results', [])
#     for video in videos:
#         if video['site'] == 'YouTube':
#             Videos.objects.get_or_create(movie=movie, type=video['type'], title=video['name'], youtube_path=f"https://www.youtube.com/embed/{video['key']}", official=video['official'], published_at=video["published_at"])


# print(Movies.objects.get(pk=244).title)
# print(User.objects.all().last())

print(People.objects.get(tmdb_id=525))
People.objects.create()


print(GenreLikes.objects.filter(user=settings.AUTH_USER_MODEL))