from django.urls import path
from . import views

urlpatterns = [
	path('', views.ApiOverview, name='home'),
    path('users', views.users),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('editprofile/<str:username>', views.editprofile),
    path('posts', views.posts),
    path('post/create', views.createpost),
    path('post/update/<str:title>', views.updatepost),
    path('post/delete/<str:title>', views.deletepost),
    path('comments', views.comments),
    path('comment/create', views.createcomment),
    path('comment/update/<int:pk>', views.updatecomment),
    path('comment/delete/<int:pk>', views.deletecomment),
    path('follow', views.follow),
    path('unfollow', views.unfollow),
    path('followers/<int:pk>', views.followers),
    path('followings/<int:pk>', views.followings),
]
