from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth import login as logins, logout as logouts
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, JsonResponse

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_user': '/users',
        'Search by name': '/users?username=user_name',
        'Register': '/register',
        'Login': '/login',
        'Logout': '/logout',
        'Edit Profile': '/editprofile/username',
        'Posts': '/posts',
        'Add Post': '/post/create',
        'Update Post': '/post/update/title',
        'Delete Post': '/post/delete/title',
        'Comments': '/comments',
        'Add Comment': '/comment/create',
        'Update Comment': '/comment/update/pk',
        'Delete Comment': '/comment/delete/pk',
        'Follow user': '/follow/pk',
        'Unfollow user': '/unfollow/pk',
        'Followers': 'followers/pk',
        'Followings': 'followings/pk',
    }
 
    return Response(api_urls)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponse('Sign up successfully!!')
    return render(request, 'signup.html', {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            logins(request, user)
            return HttpResponse('login successfully!!')
        else:
            return HttpResponse('username or password is incorrect!!')
    return render(request, 'login.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logouts(request)
            return HttpResponse('logout successfully!!')
        else:
            return HttpResponse('you are already logged out!!')
    return render(request, 'logout.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):
    if request.query_params:
        users = User.objects.filter(**request.query_params.dict())
    else:
        users = User.objects.all()
 
    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editprofile(request, username):
    user = User.objects.get(username=username)
    if user.username == request.user.username:
        data = UserSerializer(instance=user, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def posts(request):
    if request.query_params:
        posts = Post.objects.filter(**request.query_params.dict())
    else:
        posts = Post.objects.all()
 
    if posts:
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createpost(request):
    request.data['user'] = request.user.id
    post = PostSerializer(data=request.data)
 
    if post.is_valid():
        post.save()
        return Response(post.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updatepost(request, title):
    post = Post.objects.get(title=title)
    if post.user.username == request.user.username:
        request.data['user'] = request.user.id
        data = PostSerializer(instance=post, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletepost(request, title):
    post = get_object_or_404(Post, title=title)
    if post.user.username == request.user.username:
        post.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comments(request):
    if request.query_params:
        comments = Comment.objects.filter(**request.query_params.dict())
    else:
        comments = Comment.objects.all()

    if comments:
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createcomment(request):
    request.data['user'] = request.user.id
    comment = CommentSerializer(data=request.data)

    if Comment.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This comment already exists')
 
    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updatecomment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if comment.user.username == request.user.username:
        request.data['user'] = request.user.id
        data = CommentSerializer(instance=comment, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletecomment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user.username == request.user.username:
        comment.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request):
    if request.data['follower'] == request.user.id:
        follow = FollowSerializer(data=request.data)

        if Follow.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This follow already exists')
    
        if follow.is_valid():
            follow.save()
            return Response(follow.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow(request):
    if request.data['follower'] == request.user.id:
        follow = Follow.objects.get(**request.data)

        if not follow:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        follow.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers(request, pk):
    followers = Follow.objects.filter(followed=pk)
    if followers:
        serializer = FollowSerializer(followers, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followings(request, pk):
    followings = Follow.objects.filter(follower=pk)
    if followings:
        serializer = FollowSerializer(followings, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)