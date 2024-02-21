from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db import transaction
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import *
from .models import *
from accounts.models import User
from random import shuffle

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movies(request):
    movies = Movies.objects.all().order_by('-popularity')[:100]
    if request.method == 'GET':
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movies, id=movie_pk)
    if request.method == 'GET':
        serializer2 = MovieSerializer(movie)
        return Response(serializer2.data)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def top_rated(request):
    movies = Movies.objects.filter(top_rated=True).order_by('-popularity')[:20]
    if request.method == 'GET':
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def now_playing(request):
    movies = Movies.objects.filter(now_playing=True).order_by('-popularity')
    if request.method == 'GET':
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def upcoming(request):
    movies = Movies.objects.filter(upcoming=True).order_by('-popularity')
    if request.method == 'GET':
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def person_detail(request, person_pk):
    person = get_object_or_404(People, id=person_pk)
    if request.method == 'GET':
        serializer1 = PeopleSerializer(person)
        return Response(serializer1.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genre_detail(request, genre_name):
    genre = Genres.objects.get(name_en=genre_name)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        # print(genre[0])
        movies = Movies.objects.filter(genres=genre).order_by('-popularity')[:100]
        movies1 = MovieListSerializer(movies, many=True)
        return Response({ 'genre': serializer.data, 'movies': movies1.data })
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def keyword_detail(request, keyword_pk):
    keyword = Keywords.objects.get(pk=keyword_pk)
    if request.method == 'GET':
        serializer = keywordSerializer(keyword)
        movies = keyword.movies.order_by('-popularity')[:100]
        movies = MovieListSerializer(movies, many=True)
        return Response({ 'keyword': serializer.data, 'movies': movies.data })
        
        
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    genres = movie.genres.all()
    keywords = movie.keywords.all()
    if request.user in movie.like_user.all():
        s = -1
        movie.like_user.remove(request.user)
    else:
        s = 1
        movie.like_user.add(request.user)
    for genre in genres:
        print(genre.name_en)
        like = GenreLikes.objects.get_or_create(user=request.user, genre=genre)
        like[0].point += s
        like[0].save()
    for keyword in keywords:
        like = KeywordLikes.objects.get_or_create(user=request.user, keyword=keyword)
        like[0].point += s
        like[0].save()
    res = {'movieLike': movie.like_user.all().count(), 'me': False if s==-1 else True }
    return Response(res)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request, username):
    user = User.objects.get(username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        # serializer.data['keywordlikes'].sort(key=lambda x:-x['point'])
        # serializer.data['keywordlikes'] = serializer.data['keywordlikes'][0]
        # shuffle(serializer.data['keywordlikes'][0]['keyword']['movies'])
        # serializer.data['keywordlikes'][0]['keyword']['movies'] = serializer.data['keywordlikes'][0]['keyword']['movies'][:20]
        # for movie in serializer.data['keywordlikes'][0]['keyword']['movies']:
        #     movie['images'] = movie['images'][0]
        # serializer.data['genrelikes'].sort(key=lambda x:-x['point'])
        # serializer.data['genrelikes'] = serializer.data['genrelikes'][0]
        # shuffle(serializer.data['genrelikes'][0]['genre']['movies'])
        # serializer.data['genrelikes'][0]['genre']['movies'] = serializer.data['genrelikes'][0]['genre']['movies'][:20]
        # for movie in serializer.data['genrelikes'][0]['genre']['movies']:
        #     movie['images'] = movie['images'][0]
        return Response(serializer.data)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment(request, movie_id):
    movie = Movies.objects.get(pk=movie_id)
    if request.method == 'GET':
        comments = Comment.objects.filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search(request, word):
    if request.method == 'GET':
        movies1 = Movies.objects.filter(title__contains=word)
        # movies2 = Movies.objects.filter(tagline__contains=word)
        # movies3 = Movies.objects.filter(overview__contains=word)
        # keywords = Keywords.objects.filter(name__contains=word)
        genres = Genres.objects.filter(name_en__contains=word)
        people = People.objects.filter(name_en__contains=word)
        serializer1 = MovieListSerializer(movies1, many=True)
        # serializer11 = MovieListSerializer(movies2, many=True)
        # serializer12 = MovieListSerializer(movies3, many=True)
        # serializer2 = keywordSerializer(keywords, many=True)
        serializer3 = GenreSerializer(genres, many=True)
        a = serializer3
        if len(serializer3.data) > 0:
            print(Genres.objects.get(pk=serializer3.data[0]['id']).name_en)
            movies = Movies.objects.filter(genres=Genres.objects.get(pk=serializer3.data[0]['id'])).order_by('?')[:20]
            print(movies[0].title)
            a = MovieListSerializer(movies, many=True)
        serializer4 = PeopleSerializer(people, many=True)
        return Response({'movies': serializer1.data, 'genres': a.data, 'people': serializer4.data })
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def favorite(request):
    if request.method == 'GET':
        keyword = KeywordLikes.objects.filter(user=request.user).order_by('-pk').first().keyword
        kmovie = Movies.objects.filter(keywords=keyword).order_by('?')[:20]
        km = MovieListSerializer(kmovie, many=True)
        genre = GenreLikes.objects.filter(user=request.user).order_by('-point').first().genre
        gmovie = Movies.objects.filter(genres=genre).order_by('?')[:20]
        gls = MovieListSerializer(gmovie, many=True)
        genre2 = GenreLikes.objects.filter(user=request.user).order_by('-point')[1].genre
        gmovie2 = Movies.objects.filter(genres=genre2).order_by('?')[:20]
        gls2 = MovieListSerializer(gmovie2, many=True)
        # movie =get_user_model().movies_set.all().order_by('-pk').first()
        # movie = Movies.objects.filter(like_user=request.user).last()
        # rm = Movies.objects.filter(related_movie=movie)
        # m = MovieSerializer(movie)
        return Response({ 'genre': {'name': genre.name_en, 'id': genre.id, 'movies': gls.data } , 'genre2': {'name': genre2.name_en, 'id': genre2.id, 'movies': gls2.data } })
