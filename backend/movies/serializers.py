from rest_framework import serializers
from .models import *
from accounts.models import User
from django.contrib.auth import get_user_model

class keywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keywords
        fields = '__all__'
        read_only_fields = ('movies', )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('person', )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePaths
        fields = '__all__'
        read_only_fields = ('type', 'movie', 'path', )


class GenreSerializer(serializers.ModelSerializer):
    # class MovieSerializer(serializers.ModelSerializer):
    #     images = ImageSerializer(many=True, read_only=True)
    #     class Meta:
    #         model = Movies
    #         fields = ('images', 'id', 'title')
    
    # movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Genres
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    
    class RelatedSerializer(serializers.ModelSerializer):
        images = ImageSerializer(many=True, read_only=True)
        class Meta:
            model = Movies
            # fields = '__all__'
            exclude = ('related_movie', 'genres', 'like_user')
    related_movie = RelatedSerializer(many=True, read_only=True)
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', )
    genres = GenreSerializer(many=True, read_only=True)
    like_user = UserSerializer(many=True, read_only=True)
    
    class CommentSerializer(serializers.ModelSerializer):
        class US(serializers.ModelSerializer):
            class Meta:
                model=get_user_model()
                fields = ('id', 'username')
        user = US(read_only=True)
        class Meta:
            model = Comment
            exclude = ('movie',)
            read_only_fields = ('user', 'movie' )
    comment = CommentSerializer(many=True, read_only=True)
    class CreditSerializer(serializers.ModelSerializer):
        # class MovieSerializer(serializers.ModelSerializer):
        #     images = ImageSerializer(many=True, read_only=True)
        #     class Meta:
        #         model = Movies
        #         fields = ('title', 'images')
        #         read_only_fields = ('genres', 'related_movie', )
        # movie = MovieSerializer(read_only=True)
        class PeopleSerializer(serializers.ModelSerializer):
            class ProfileSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Profile
                    fields = '__all__'
                    read_only_fields = ('person', )
            profile = ProfileSerializer(many=True, read_only=True)
            class Meta:
                model = People
                fields = ('id', 'profile', 'name_en')
        person = PeopleSerializer(read_only=True)
        class Meta:
            model = Credits
            fields = ('character', 'role', 'person', )
            read_only_fields = ('movie', 'person', 'role', )
    credits = CreditSerializer(many=True, read_only=True)
    keywords = keywordSerializer(many=True, read_only=True)
    class VideoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Videos
            fields = '__all__'
            read_only_fields = ('movie', )
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Movies
        fields = '__all__'
        read_only_fields = ('genres', 'related_movie', )


class MovieListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username')
    like_user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Movies
        exclude = ('genres', 'related_movie', )
        read_only_fields = ('genres', 'related_movie', )
        

class CreditSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Credits
        fields = ('character', 'role', 'person', 'movie')
        read_only_fields = ('movies', 'person', 'role', )


class PeopleSerializer(serializers.ModelSerializer):
    class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = '__all__'
            read_only_fields = ('person', )
    profile = ProfileSerializer(many=True, read_only=True)
    
    credits = CreditSerializer(many=True, read_only=True) 
    class Meta:
        model = People
        fields = '__all__'
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'
        read_only_fields = ('movie', )


class UserSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class ImagePath(serializers.ModelSerializer):
            class Meta:
                model = ImagePaths
                fields = ('path', 'type')
        class User(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('id', 'username')
        images = ImagePath(many=True, read_only=True)
        like_user = User(many=True, read_only=True)
        class Meta:
            model = Movies
            fields = ('id', 'title', 'images', 'like_user')
    movies_set = MovieListSerializer(many=True, read_only=True)

    class CommentSerializer(serializers.ModelSerializer):
        class MovieSerializer(serializers.ModelSerializer):
            class ImagePath(serializers.ModelSerializer):
                class Meta:
                    model = ImagePaths
                    fields = ('path', 'type')
            
            images = ImagePath(many=True, read_only=True)
            class Meta:
                model = Movies
                fields = ('id', 'images', 'title', )
        movie = MovieSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('user', 'movie' )

    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username','comment', 'movies_set',)

        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'movie' )


class KLS(serializers.ModelSerializer):
    keyword = keywordSerializer(read_only=True)
    class Meta:
        model = KeywordLikes
        fields = '__all__'
        read_only_fields = ('user', 'keyword' )


class GLS(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    class Meta:
        model = GenreLikes
        fields = '__all__'
        read_only_fields = ('user', 'genre' )
