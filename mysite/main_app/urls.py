from django.urls import path
from .views import *

urlpatterns =[
    path('', MainAppHome.as_view(), name="home"),
    path('login/', LoginUser.as_view(), name="login"),
    path('registration/', RegisterUser.as_view(), name="register"),
    path('logout/', logout_user, name="logout"),
    path('create/', CreatePost.as_view(), name="create"),
    path('post//anime/<slug:anime_slug>/', ShowPostAnime.as_view(), name='post'),
    path('post/manga/<slug:manga_slug>/', ShowPostManga.as_view(), name='post'),
    path('post/<slug:anime_slug>/edit/', EditPost.as_view(), name="edit"),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name="category"),
    path('studio/<slug:st_slug>/', ShowStudio.as_view(), name="studio"),
    path('person/<slug:person_slug>/', ShowStudio.as_view(), name="person"),
    path('character/<slug:char_slug>/', ShowStudio.as_view(), name="character"),
]
