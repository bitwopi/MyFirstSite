from django.urls import path
from .views import *

urlpatterns =[
    path('', MainAppHome.as_view(), name="home"),
    path('login/', LoginUser.as_view(), name="login"),
    path('registration/', RegisterUser.as_view(), name="register"),
    path('logout/', logout_user, name="logout"),
    path('create/', CreatePost.as_view(), name="create"),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('post/<slug:post_slug>/edit/', EditPost.as_view(), name="edit"),
]
