import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import requests


# from movies.models import People

# people = People.objects.all()
# for person in people:
#     url = f'https://api.themoviedb.org/3/person/{person.tmdb_id}/movie_credits?api_key=e95b79709ef9e216e667b4d9554f60f5'


from movies.models import People, Roles, Movies, Credits, Genres

# print(Credits.objects.filter(movie=Movies.objects.get(pk=4479)))

# people = Movies.objects.get(pk=4479).credit.all().person.all()
# for person in people:
#     print(person.name_en)

# for a in Credits.objects.filter(movie=Movies.objects.get(pk=5679)):
#     print(a.person.name_en)

# for movie in Movies.genres.all(Genres.objects.get(name_ko='액션')):
#     print(movie.title)


for movie in Genres.objects.get(name_ko='액션').movie.all():
    print(movie.title)
