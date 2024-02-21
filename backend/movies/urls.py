from django.urls import path
from . import views

urlpatterns = [
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('movies/', views.movies),
    path('movies/top_rated/', views.top_rated),
    path('movies/now_playing/', views.now_playing),
    path('movies/upcoming/', views.upcoming),
    path('person/<int:person_pk>/', views.person_detail),
    path('genre/<str:genre_name>/', views.genre_detail),
    path('keyword/<int:keyword_pk>/', views.keyword_detail),
    path('likes/<int:movie_id>/', views.likes),
    path('user/<str:username>/', views.user),
    path('comments/movie/<int:movie_id>/', views.comment),
    path('userfavorite/', views.favorite),
]

