import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import requests
## 데이터 import 하려면 위에 있는 코드는 필수!!


# # genre 데이터 import 하는 코드(완료)
# genresEN = [
#     {
#       "id": 28,
#       "name": "Action"
#     },
#     {
#       "id": 12,
#       "name": "Adventure"
#     },
#     {
#       "id": 16,
#       "name": "Animation"
#     },
#     {
#       "id": 35,
#       "name": "Comedy"
#     },
#     {
#       "id": 80,
#       "name": "Crime"
#     },
#     {
#       "id": 99,
#       "name": "Documentary"
#     },
#     {
#       "id": 18,
#       "name": "Drama"
#     },
#     {
#       "id": 10751,
#       "name": "Family"
#     },
#     {
#       "id": 14,
#       "name": "Fantasy"
#     },
#     {
#       "id": 36,
#       "name": "History"
#     },
#     {
#       "id": 27,
#       "name": "Horror"
#     },
#     {
#       "id": 10402,
#       "name": "Music"
#     },
#     {
#       "id": 9648,
#       "name": "Mystery"
#     },
#     {
#       "id": 10749,
#       "name": "Romance"
#     },
#     {
#       "id": 878,
#       "name": "Science Fiction"
#     },
#     {
#       "id": 10770,
#       "name": "TV Movie"
#     },
#     {
#       "id": 53,
#       "name": "Thriller"
#     },
#     {
#       "id": 10752,
#       "name": "War"
#     },
#     {
#       "id": 37,
#       "name": "Western"
#     }
#   ]
# genresKO = [
#     {
#       "id": 28,
#       "name": "액션"
#     },
#     {
#       "id": 12,
#       "name": "모험"
#     },
#     {
#       "id": 16,
#       "name": "애니메이션"
#     },
#     {
#       "id": 35,
#       "name": "코미디"
#     },
#     {
#       "id": 80,
#       "name": "범죄"
#     },
#     {
#       "id": 99,
#       "name": "다큐멘터리"
#     },
#     {
#       "id": 18,
#       "name": "드라마"
#     },
#     {
#       "id": 10751,
#       "name": "가족"
#     },
#     {
#       "id": 14,
#       "name": "판타지"
#     },
#     {
#       "id": 36,
#       "name": "역사"
#     },
#     {
#       "id": 27,
#       "name": "공포"
#     },
#     {
#       "id": 10402,
#       "name": "음악"
#     },
#     {
#       "id": 9648,
#       "name": "미스터리"
#     },
#     {
#       "id": 10749,
#       "name": "로맨스"
#     },
#     {
#       "id": 878,
#       "name": "SF"
#     },
#     {
#       "id": 10770,
#       "name": "TV 영화"
#     },
#     {
#       "id": 53,
#       "name": "스릴러"
#     },
#     {
#       "id": 10752,
#       "name": "전쟁"
#     },
#     {
#       "id": 37,
#       "name": "서부"
#     }
#   ]

# from movies.models import Genres

# for i in range(19):
#     Genres.objects.create(tmdbId=genresEN[i]['id'], nameEN=genresEN[i]['name'], nameKO=genresKO[i]['name'])


# people 데이터 import하는 코드
# from movies.models import People

# for i in range(2, 10000):
#     try:
#         URL = f'https://api.themoviedb.org/3/person/{i}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response = requests.get(URL)
#         data = response.json()
#         a = People.objects.create(tmdb_id=data['id'], name_en=data['name'], name_ko=data['name'],popularity=data['popularity'], profile='https://www.themoviedb.org/t/p/w300_and_h450_bestv2'+data['profile_path'], imdb_id=data["imdb_id"])
#     except:
#         continue


# # 역할 추가
# Roles.objects.create(department_en='Cast', department_ko='출연')
# Roles.objects.create(department_en='Director', department_ko='감독')





from movies.models import People, Roles, Movies, Credits, Genres, ImageTypes, ImagePaths, Videos, Keywords

# credit 추가하는 코드
# people = People.objects.all()
# for person in people:
#     id = person.tmdb_id
#     URL = f'https://api.themoviedb.org/3/person/{id}/movie_credits?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(URL)
#     data = response.json()
    
#     movies = data['cast']
#     for movie in movies:
#         try:
#             aa = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#         except:
#             print(movie['id'], person.tmdb_id)    
#         Credits.objects.update_or_create(movie=aa[0], person=person, role=Roles.objects.get(department_en='Cast'), character= movie['character'])
#     movies = data['crew']
#     for movie in movies:
#         if movie['department'] == 'Directing':
#             ab = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
    
#             Credits.objects.update_or_create(movie=ab[0], person=person, role=Roles.objects.get(department_en='Director'))
   
# # try 에러 (popular 탭이 없음)
# # 1173608 108
# # 407945 613
# # 337757 682
# # 109701 1146

# # 다음에 시간나면 더 하기

# 영화에 장르 넣는 함수
# 한 번에 요청 제한 걸린듯
# 데이터 import 이어서
# movies = Movies.objects.all()
# for movie in movies:
#     id = movie.tmdb_id
#     URL = f'https://api.themoviedb.org/3/movie/{id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(URL)
#     data = response.json()
#     genres = data['genres']
#     for genre in genres:
#         movie.genres.add(Genres.objects.get(tmdb_id=genre['id']))


# # imagetype 모델 데이터 넣기
# ImageTypes.objects.create(type='backdrops')
# ImageTypes.objects.create(type='logos')
# ImageTypes.objects.create(type='posters')


# # 장르 데이터 넣기
# for i in range(62145, 62165):
#     movie = Movies.objects.get(pk=i)
#     id = movie.tmdb_id
#     URL = f'https://api.themoviedb.org/3/movie/{id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(URL)
#     data = response.json()
#     genres = data.get('genres', [])
#     for genre in genres:
#         movie.genres.add(Genres.objects.get(tmdb_id=genre['id']))





# imagepath 모델 데이터 넣기
movies = Movies.objects.all()
for movie in movies:
    id = movie.tmdb_id
    url = f'https://api.themoviedb.org/3/movie/{id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
    response = requests.get(url)
    data = response.json()
    images = data.get('backdrops', [])
    for image in images:
        ImagePaths.objects.update_or_create(type=ImageTypes.objects.get(type='backdrops'), path=f'https://www.themoviedb.org/t/p/w{image["width"]}_and_h{image["height"]}_bestv2{image["file_path"]}', movie=movie, ratio=image["aspect_ratio"], defaults={'path': f'https://www.themoviedb.org/t/p/original{image["file_path"]}'})
    images = data.get('logos', [])
    for image in images:
        ImagePaths.objects.update_or_create(type=ImageTypes.objects.get(type='logos'), path=f'https://www.themoviedb.org/t/p/w{image["width"]}_and_h{image["height"]}_bestv2{image["file_path"]}', movie=movie, ratio=image["aspect_ratio"], defaults={'path': f'https://www.themoviedb.org/t/p/original{image["file_path"]}'})
    images = data.get('posters', [])
    for image in images:
        ImagePaths.objects.update_or_create(type=ImageTypes.objects.get(type='posters'), path=f'https://www.themoviedb.org/t/p/w{image["width"]}_and_h{image["height"]}_bestv2{image["file_path"]}', movie=movie, ratio=image["aspect_ratio"], defaults={'path': f'https://www.themoviedb.org/t/p/original{image["file_path"]}'})


# # video 데이터 넣기
# movies = Movies.objects.all()
# for movie in movies:
#     id = movie.tmdb_id
#     url = f'https://api.themoviedb.org/3/movie/{id}/videos?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(url)
#     data = response.json()
#     videos = data.get('results', [])
#     for video in videos:
#         if video['site'] == 'YouTube':
#             Videos.objects.create(movie=movie, type=video['type'], title=video['title'], youtube_key=f"https://www.youtube.com/embed/{video['key']}", official=video['official'], published_at=video["published_at"])


# # 키워드 데이터 넣기
# movies = Movies.objects.all()
# for movie in movies:
#     id = movie.tmdb_id
#     url = f'https://api.themoviedb.org/3/movie/{id}/keywords?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(url)
#     data = response.json()
#     keywords = data.get('keywords', [])
#     for keyword in keywords:
#         Keywords.objects.get_or_create(tmdb_id=keyword['id'], defaults={'name': keyword['name'], 'movies': movie})


# now_playing = models.BooleanField(default=False)
# top_rated = models.BooleanField(default=False)
# upcoming = models.BooleanField(default=False)

# # now_playing 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/now_playing?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['result']
# for movie in movies:
#     a = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#     a.now_playing = True

# # top_ rated 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/top_rated?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['result']
# for movie in movies:
#     a = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#     a.top_rated = True



# # upcoming 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/upcoming?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['result']
# for movie in movies:
#     a = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#     a.upcoming = True

# # related_movie 데이터 추가
# movies = Movies.objects.all()
# for movie in movies:
#     id = movie.tmdb_id
#     url = f'https://api.themoviedb.org/3/movie/{id}/recommendations?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response = requests.get(url)
#     data = response.json()
#     results = data.get('results', [])
#     for result in results:
#         a = Movies.objects.get_or_create(tmdb_id=movie['id'], defaults={'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#         movie.related_movie.add(a)