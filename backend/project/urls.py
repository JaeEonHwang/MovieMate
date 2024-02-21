from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movies.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('likes/<int:movie_id>/', views.likes),
    path('user/<int:username>/', views.user),
    path('accounts/', include('allauth.urls')),
    path('search/<str:word>/', views.search),
]

