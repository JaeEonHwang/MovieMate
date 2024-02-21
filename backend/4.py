import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import requests

from movies.models import People, Roles, Movies, Credits, Genres, ImageTypes, ImagePaths, Videos, Keywords, Profile

# Movies.objects.create(adult=False, tmdb_id=1, overview='overview', popularity=123, release_date='2023-11-17', title='title', now_playing=False, top_rated=True, upcoming=False)

# # 장르 넣기
# url = f'https://api.themoviedb.org/3/genre/movie/list?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# for genre in data['genres']:
#     Genres.objects.update_or_create(tmdb_id=genre['id'], defaults={'name_en': genre['name'], 'name_ko': genre['name']})


# # 롤 넣기
# Roles.objects.create(department_en='Director', department_ko='감독')
# Roles.objects.create(department_en='Cast', department_ko='출연')


# # 이미지 타입 넣기기
# ImageTypes.objects.create(type='backdrops')
# ImageTypes.objects.create(type='posters')
# ImageTypes.objects.create(type='logos')


# Movies.objects.all().delete()
# People.objects.all().delete()
# Profile.objects.all().delete()
# Credits.objects.all().delete()
# ImagePaths.objects.all().delete()
# Videos.objects.all().delete()

# # now_playing 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/now_playing?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['results']
# for movie0 in movies:
#     #영화 추가
#     movie_id = movie0['id']
#     url1 = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response1 = requests.get(url1)
#     movie = response1.json()
#     obj = Movies.objects.update_or_create(tmdb_id=movie_id, defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title'], 'now_playing': True })
#     if obj[1]:
#         obj = obj[0]
#         # 장르 추가
#         genres = movie.get('genres', [])
#         for genre in genres:
#             obj.genres.add(Genres.objects.get(tmdb_id=genre['id']))
#         # 이미지 추가
#         url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response2 = requests.get(url2)
#         data2 = response2.json()
#         for backdrop in data2.get('backdrops', []):
#             if backdrop["aspect_ratio"] == 1.778:
#                 ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='backdrops'))
#         for backdrop in data2.get('posters', []):
#             if backdrop["aspect_ratio"] == 0.667:
#                 ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='posters'))
#         # 비디오 추가       
#         url3 = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response3 = requests.get(url3)
#         data3 = response3.json()
#         videos = data3.get('results', [])
#         for video in videos:
#             if video['site'] == 'YouTube':
#                 Videos.objects.create(movie=obj, type=video['type'], title=video['name'], youtube_path=f"https://www.youtube.com/embed/{video['key']}", official=video['official'], published_at=video["published_at"])
#         # 레코멘데이션
#         url4 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response4 = requests.get(url4)
#         data4 = response4.json()
#         results = data4.get('results', [])
#         for result in results:
#             url1 = f'https://api.themoviedb.org/3/movie/{result["id"]}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response1 = requests.get(url1)
#             movie = response1.json()
#             a = Movies.objects.update_or_create(tmdb_id=result["id"], defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#             obj.related_movie.add(a[0])
#         # 키워드 추가
#         url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response5 = requests.get(url5)
#         data5 = response5.json()
#         results = data5.get('keywords', [])
#         for keyword in results:
#             key=Keywords.objects.get_or_create(tmdb_id=keyword['id'], defaults={'name': keyword['name']})
#             key[0].movies.add(obj)
    
#         # 크레딧 추가
#         url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response5 = requests.get(url5)
#         data5 = response5.json()
#         num = 0
#         for cast in data5.get('cast', []):
#             person_id = cast['id']
#             url6 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response6 = requests.get(url6)
#             data6 = response6.json()
#             peo=People.objects.update_or_create(tmdb_id=data6['id'], defaults={'birthday': data6.get('birthday', ''), 'name_en': data6['name'], 'popularity': data6.get('popularity', 0), 'imdb_id' :data6.get('imdb_id', '')})
#             Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=2), character=cast.get('character', ''))
#             url6 = f'https://api.themoviedb.org/3/person/{person_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response6 = requests.get(url6)
#             data6 = response6.json()
#             for profile in data6.get('profiles', []):
#                 if profile['aspect_ratio'] == 0.667:
#                     Profile.objects.create(person=peo[0], profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
#             num += 1
#             if num == 10:
#                 break
#         for crew in data5.get('crew', []):
#             if crew.get('job', '') == 'Director':
#                 person_id = cast['id']
#                 url7 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#                 response7 = requests.get(url7)
#                 data7 = response7.json()
#                 peo=People.objects.update_or_create(tmdb_id=data7['id'], defaults={'birthday': data7.get('birthday', ''), 'name_en': data7['name'], 'name_ko': data7['name'], 'popularity': data7.get('popularity', 0), 'imdb_id': data7.get('imdb_id', '')})
#                 Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=1))
#                 url6 = f'https://api.themoviedb.org/3/person/{person_id}/images'
#                 response6 = requests.get(url6)
#                 data6 = response6.json()
#                 # 프로필 추가
#                 for profile in data6.get('profiles', []):
#                     if profile['aspect_ratio'] == 0.667:
#                         Profile.objects.create(person=peo, profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
#                 break
            
    
# # # upcoming 데이터 추가
# url = f'https://api.themoviedb.org/3/movie/upcoming?api_key=e95b79709ef9e216e667b4d9554f60f5'
# response = requests.get(url)
# data = response.json()
# movies = data['results']
# for movie0 in movies:
#     #영화 추가
#     movie_id = movie0['id']
#     url1 = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#     response1 = requests.get(url1)
#     movie = response1.json()
#     obj = Movies.objects.update_or_create(tmdb_id=movie_id, defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title'], 'upcoming': True })
#     if obj[1]:
#         obj = obj[0]
#         # 장르 추가
#         genres = movie.get('genres', [])
#         for genre in genres:
#             obj.genres.add(Genres.objects.get(tmdb_id=genre['id']))
#         # 이미지 추가
#         url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response2 = requests.get(url2)
#         data2 = response2.json()
#         for backdrop in data2.get('backdrops', []):
#             if backdrop["aspect_ratio"] == 1.778:
#                 ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='backdrops'))
#         for backdrop in data2.get('posters', []):
#             if backdrop["aspect_ratio"] == 0.667:
#                 ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='posters'))
#         # 비디오 추가       
#         url3 = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response3 = requests.get(url3)
#         data3 = response3.json()
#         videos = data3.get('results', [])
#         for video in videos:
#             if video['site'] == 'YouTube':
#                 Videos.objects.create(movie=obj, type=video['type'], title=video['name'], youtube_path=f"https://www.youtube.com/embed/{video['key']}", official=video['official'], published_at=video["published_at"])
#         # 레코멘데이션
#         url4 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response4 = requests.get(url4)
#         data4 = response4.json()
#         results = data4.get('results', [])
#         for result in results:
#             url1 = f'https://api.themoviedb.org/3/movie/{result["id"]}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response1 = requests.get(url1)
#             movie = response1.json()
#             a = Movies.objects.update_or_create(tmdb_id=result["id"], defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#             obj.related_movie.add(a[0])
#         # 키워드 추가
#         url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response5 = requests.get(url5)
#         data5 = response5.json()
#         results = data5.get('keywords', [])
#         for keyword in results:
#             key=Keywords.objects.get_or_create(tmdb_id=keyword['id'], defaults={'name': keyword['name']})
#             key[0].movies.add(obj)
    
#         # 크레딧 추가
#         url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response5 = requests.get(url5)
#         data5 = response5.json()
#         num = 0
#         for cast in data5.get('cast', []):
#             person_id = cast['id']
#             url6 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response6 = requests.get(url6)
#             data6 = response6.json()
#             peo=People.objects.update_or_create(tmdb_id=data6['id'], defaults={'birthday': data6.get('birthday', ''), 'name_en': data6['name'], 'popularity': data6.get('popularity', 0), 'imdb_id' :data6.get('imdb_id', '')})
#             Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=2), character=cast.get('character', ''))
#             url6 = f'https://api.themoviedb.org/3/person/{person_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response6 = requests.get(url6)
#             data6 = response6.json()
#             for profile in data6.get('profiles', []):
#                 if profile['aspect_ratio'] == 0.667:
#                     Profile.objects.create(person=peo[0], profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
#             num += 1
#             if num == 10:
#                 break
#         for crew in data5.get('crew', []):
#             if crew.get('job', '') == 'Director':
#                 person_id = cast['id']
#                 url7 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#                 response7 = requests.get(url7)
#                 data7 = response7.json()
#                 peo=People.objects.update_or_create(tmdb_id=data7['id'], defaults={'birthday': data7.get('birthday', ''), 'name_en': data7['name'], 'name_ko': data7['name'], 'popularity': data7.get('popularity', 0), 'imdb_id': data7.get('imdb_id', '')})
#                 Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=1))
#                 url6 = f'https://api.themoviedb.org/3/person/{person_id}/images'
#                 response6 = requests.get(url6)
#                 data6 = response6.json()
#                 # 프로필 추가
#                 for profile in data6.get('profiles', []):
#                     if profile['aspect_ratio'] == 0.667:
#                         Profile.objects.create(person=peo, profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
#                 break


# # # top_ rated 데이터 추가
# for i in range(1, 450):
#     url = f'https://api.themoviedb.org/3/movie/top_rated?api_key=e95b79709ef9e216e667b4d9554f60f5&page={i}'
#     response = requests.get(url)
#     data = response.json()
#     movies = data['results']
#     for movie0 in movies:
#         #영화 추가
#         movie_id = movie0['id']
#         url1 = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#         response1 = requests.get(url1)
#         movie = response1.json()
#         obj = Movies.objects.update_or_create(tmdb_id=movie_id, defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title'], 'top_rated': True if i < 21 else False })
#         if obj[1]:
#             obj = obj[0]
#             # 장르 추가
#             genres = movie.get('genres', [])
#             for genre in genres:
#                 obj.genres.add(Genres.objects.get(tmdb_id=genre['id']))
#             # 이미지 추가
#             url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response2 = requests.get(url2)
#             data2 = response2.json()
#             for backdrop in data2.get('backdrops', []):
#                 if backdrop["aspect_ratio"] == 1.778:
#                     ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='backdrops'))
#             for backdrop in data2.get('posters', []):
#                 if backdrop["aspect_ratio"] == 0.667:
#                     ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='posters'))
#             # 비디오 추가       
#             url3 = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response3 = requests.get(url3)
#             data3 = response3.json()
#             videos = data3.get('results', [])
#             for video in videos:
#                 if video['site'] == 'YouTube':
#                     Videos.objects.create(movie=obj, type=video['type'], title=video['name'], youtube_path=f"https://www.youtube.com/embed/{video['key']}", official=video['official'], published_at=video["published_at"])
#             # 레코멘데이션
#             url4 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response4 = requests.get(url4)
#             data4 = response4.json()
#             results = data4.get('results', [])
#             for result in results:
#                 url1 = f'https://api.themoviedb.org/3/movie/{result["id"]}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#                 response1 = requests.get(url1)
#                 movie = response1.json()
#                 a = Movies.objects.update_or_create(tmdb_id=result["id"], defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
#                 obj.related_movie.add(a[0])
#             # 키워드 추가
#             url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response5 = requests.get(url5)
#             data5 = response5.json()
#             results = data5.get('keywords', [])
#             for keyword in results:
#                 key=Keywords.objects.get_or_create(tmdb_id=keyword['id'], defaults={'name': keyword['name']})
#                 key[0].movies.add(obj)
        
#             # 크레딧 추가
#             url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e95b79709ef9e216e667b4d9554f60f5'
#             response5 = requests.get(url5)
#             data5 = response5.json()
#             num = 0
#             for cast in data5.get('cast', []):
#                 person_id = cast['id']
#                 url6 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#                 response6 = requests.get(url6)
#                 data6 = response6.json()
#                 peo=People.objects.update_or_create(tmdb_id=data6['id'], defaults={'birthday': data6.get('birthday', ''), 'name_en': data6['name'], 'popularity': data6.get('popularity', 0), 'imdb_id' :data6.get('imdb_id', '')})
#                 Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=2), character=cast.get('character', ''))
#                 url6 = f'https://api.themoviedb.org/3/person/{person_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
#                 response6 = requests.get(url6)
#                 data6 = response6.json()
#                 for profile in data6.get('profiles', []):
#                     if profile['aspect_ratio'] == 0.667:
#                         Profile.objects.create(person=peo[0], profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
#                 num += 1
#                 if num == 10:
#                     break
#             for crew in data5.get('crew', []):
#                 if crew.get('job', '') == 'Director':
#                     person_id = cast['id']
#                     url7 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
#                     response7 = requests.get(url7)
#                     data7 = response7.json()
#                     peo=People.objects.update_or_create(tmdb_id=data7['id'], defaults={'birthday': data7.get('birthday', ''), 'name_en': data7['name'], 'name_ko': data7['name'], 'popularity': data7.get('popularity', 0), 'imdb_id': data7.get('imdb_id', '')})
#                     Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=1))
#                     url6 = f'https://api.themoviedb.org/3/person/{person_id}/images'
#                     response6 = requests.get(url6)
#                     data6 = response6.json()
#                     # 프로필 추가
#                     for profile in data6.get('profiles', []):
#                         if profile['aspect_ratio'] == 0.667:
#                             Profile.objects.create(person=peo, profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
#                     break




movies = Movies.objects.order_by('related_movie')
for movie0 in movies:
    if movie0.related_movie.all():
        break
    #영화 추가
    movie_id = movie0.tmdb_id
    url1 = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
    response1 = requests.get(url1)
    movie = response1.json()
    obj = Movies.objects.update_or_create(tmdb_id=movie_id, defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
    obj = obj[0]
    if not obj.genres.all():
        # 장르 추가
        genres = movie.get('genres', [])
        for genre in genres:
            obj.genres.add(Genres.objects.get(tmdb_id=genre['id']))
    if not obj.images.all():
        # 이미지 추가
        url2 = f'https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
        response2 = requests.get(url2)
        data2 = response2.json()
        for backdrop in data2.get('backdrops', []):
            if backdrop["aspect_ratio"] == 1.778:
                ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='backdrops'))
        for backdrop in data2.get('posters', []):
            if backdrop["aspect_ratio"] == 0.667:
                ImagePaths.objects.create(movie=obj, path=f'https://image.tmdb.org/t/p/original{backdrop["file_path"]}', type = ImageTypes.objects.get(type='posters'))
    if not obj.videos.all():
        # 비디오 추가       
        url3 = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=e95b79709ef9e216e667b4d9554f60f5'
        response3 = requests.get(url3)
        data3 = response3.json()
        videos = data3.get('results', [])
        for video in videos:
            if video['site'] == 'YouTube':
                Videos.objects.create(movie=obj, type=video['type'], title=video['name'], youtube_path=f"https://www.youtube.com/embed/{video['key']}", official=video['official'], published_at=video["published_at"])
    if not obj.related_movie.all():    
        # 레코멘데이션
        url4 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=e95b79709ef9e216e667b4d9554f60f5'
        response4 = requests.get(url4)
        data4 = response4.json()
        results = data4.get('results', [])
        for result in results:
            url1 = f'https://api.themoviedb.org/3/movie/{result["id"]}?api_key=e95b79709ef9e216e667b4d9554f60f5'
            response1 = requests.get(url1)
            movie = response1.json()
            a = Movies.objects.update_or_create(tmdb_id=result["id"], defaults={'imdb_id':movie['imdb_id'], 'homepage': movie['homepage'], 'runtime': movie['runtime'], 'adult': movie['adult'], 'overview': movie['overview'], 'popularity': movie['popularity'], 'release_date': movie['release_date'], 'title': movie['title']})
            obj.related_movie.add(a[0])
    if not obj.keywords.all(): 
        # 키워드 추가
        url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key=e95b79709ef9e216e667b4d9554f60f5'
        response5 = requests.get(url5)
        data5 = response5.json()
        results = data5.get('keywords', [])
        for keyword in results:
            key=Keywords.objects.get_or_create(tmdb_id=keyword['id'], defaults={'name': keyword['name']})
            key[0].movies.add(obj)
    # 크레딧 추가
    if not obj.credits.all():
        url5 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e95b79709ef9e216e667b4d9554f60f5'
        response5 = requests.get(url5)
        data5 = response5.json()
        num = 0
        for cast in data5.get('cast', []):
            person_id = cast['id']
            url6 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
            response6 = requests.get(url6)
            data6 = response6.json()
            peo=People.objects.update_or_create(tmdb_id=data6['id'], defaults={'birthday': data6.get('birthday', ''), 'name_en': data6['name'], 'popularity': data6.get('popularity', 0), 'imdb_id' :data6.get('imdb_id', '')})
            Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=2), character=cast.get('character', ''))
            url6 = f'https://api.themoviedb.org/3/person/{person_id}/images?api_key=e95b79709ef9e216e667b4d9554f60f5'
            response6 = requests.get(url6)
            data6 = response6.json()
            for profile in data6.get('profiles', []):
                if profile['aspect_ratio'] == 0.667:
                    Profile.objects.create(person=peo[0], profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
            num += 1
            if num == 10:
                break
        for crew in data5.get('crew', []):
            if crew.get('job', '') == 'Director':
                person_id = cast['id']
                url7 = f'https://api.themoviedb.org/3/person/{person_id}?api_key=e95b79709ef9e216e667b4d9554f60f5'
                response7 = requests.get(url7)
                data7 = response7.json()
                peo=People.objects.update_or_create(tmdb_id=data7['id'], defaults={'birthday': data7.get('birthday', ''), 'name_en': data7['name'], 'name_ko': data7['name'], 'popularity': data7.get('popularity', 0), 'imdb_id': data7.get('imdb_id', '')})
                Credits.objects.create(movie=obj, person=peo[0], role=Roles.objects.get(pk=1))
                url6 = f'https://api.themoviedb.org/3/person/{person_id}/images'
                response6 = requests.get(url6)
                data6 = response6.json()
                # 프로필 추가
                for profile in data6.get('profiles', []):
                    if profile['aspect_ratio'] == 0.667:
                        Profile.objects.create(person=peo, profile_path=f'https://www.themoviedb.org/t/p/original{profile["file_path"]}')
                break
            
            
# 프로필은 다음에 따로 확인