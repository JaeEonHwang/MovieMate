from django.db import models
from django.conf import settings

# Create your models here.
class Genres(models.Model):
    tmdb_id = models.IntegerField(unique=True, blank=False)
    name_en = models.CharField(max_length=20, unique=True, blank=False)
    name_ko = models.CharField(max_length=20, unique=True, blank=True)


class People(models.Model):
    tmdb_id = models.IntegerField(unique=True, blank=False)
    imdb_id = models.CharField(max_length=20, null=True)
    birthday = models.CharField(max_length=20, null=True)
    name_en = models.CharField(max_length=100, blank=False)
    popularity = models.FloatField(blank=False)
    


class Profile(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE, related_name='profile', blank=False)
    profile_path = models.CharField(max_length=100, blank=False, default='https://media.istockphoto.com/id/1164822188/vector/male-avatar-profile-picture.jpg?s=612x612&w=0&k=20&c=KPsLgVIwEGdDvf4_kiynCXw96p_PhBjIGdU68qkpbuI=')


class Roles(models.Model):
    department_en = models.CharField(max_length=20, blank=False, unique=True)
    department_ko = models.CharField(max_length=20, default=department_en, unique=True)


class ImageTypes(models.Model):
    type = models.CharField(max_length=20, blank=False, unique=True)
    

class Movies(models.Model):
    tmdb_id = models.IntegerField(unique=True, blank=False)
    imdb_id = models.CharField(max_length=20, null=True)
    adult = models.BooleanField(blank=False)
    homepage = models.CharField(max_length=100, blank=True)
    overview = models.TextField(blank=True, default='')
    popularity = models.FloatField(blank=False, default=0)
    release_date = models.CharField(max_length=20, blank=False)
    runtime = models.IntegerField(blank=False, default=0)
    title = models.CharField(max_length=100, blank=False)
    tagline = models.CharField(max_length=200, default='')
    now_playing = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)
    upcoming = models.BooleanField(default=False)
    genres = models.ManyToManyField(Genres, related_name='movies')
    related_movie = models.ManyToManyField('self', symmetrical=False)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Credits(models.Model):
    movie = models.ForeignKey(Movies, blank=False, on_delete=models.CASCADE, related_name='credits')
    person = models.ForeignKey(People, blank=False, on_delete=models.CASCADE, related_name='credits')
    role = models.ForeignKey(Roles, blank=False, on_delete=models.CASCADE)
    character = models.CharField(max_length=100, blank=True)


class ImagePaths(models.Model):
    type = models.ForeignKey(ImageTypes, blank=False, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, blank=False, on_delete=models.CASCADE, related_name='images')
    path = models.CharField(max_length=100, blank=False)

class Videos(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, blank=False, related_name='videos')
    type = models.CharField(max_length=20, blank=False)
    title = models.CharField(max_length=100, blank=False)
    youtube_path = models.CharField(max_length=100, blank=False)
    official = models.BooleanField(blank=False)
    published_at = models.CharField(max_length=50, blank=False)


class Keywords(models.Model):
    tmdb_id = models.IntegerField(unique=True, blank=False)
    name = models.CharField(max_length=20, blank=False, unique=True)
    movies = models.ManyToManyField(Movies, related_name='keywords')



class KeywordLikes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='keywordlikes')
    keyword = models.ForeignKey(Keywords, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)

class GenreLikes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='genrelikes')
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comment')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# migrate 필요
# 영화 관련 더 만들어야할 모델
# movies - recommendation: 영화별 추천 영화 (symmetrial 주의 N:M 이틀차 참고)
# movie lists - now playing, popular, top rated, upcoming

