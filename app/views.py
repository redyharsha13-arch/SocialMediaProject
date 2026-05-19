from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from .models import Profile, Post, Comment, Like, Follow
from .forms import SignupForm, LoginForm, PostForm, CommentForm, ProfileEditForm


# ---------------- HOME ----------------
def home(request):
    posts = Post.objects.all().select_related('user', 'user__profile')

    liked_posts = set()
    if request.user.is_authenticated:
        liked_posts = set(
            Like.objects.filter(user=request.user).values_list('post_id', flat=True)
        )

    posts_data = []
    for post in posts:
        posts_data.append({
            'post': post,
            'comments': post.comments.select_related('user').all(),
            'is_liked': post.id in liked_posts,
            'likes_count': post.likes.count(),
            'comments_count': post.comments.count(),
        })

    return render(request, 'home.html', {
        'posts_data': posts_data,
    })


# ---------------- SIGNUP ----------------
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        Profile.objects.get_or_create(user=user)   # 🔥 IMPORTANT FIX
        login(request, user)
        return redirect('home')

    return render(request, 'signup.html', {'form': form})


# ---------------- LOGIN ----------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user:
            Profile.objects.get_or_create(user=user)  # 🔥 CRITICAL FIX
            login(request, user)
            return redirect('home')

        messages.error(request, "Invalid credentials")

    return render(request, 'login.html', {'form': form})


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- CREATE POST ----------------
@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('home')

    return render(request, 'create_post.html', {'form': form})


# ---------------- DELETE POST ----------------
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    return redirect('home')


# ---------------- PROFILE ----------------
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)

    # 🔥 SAFE PROFILE HANDLING (FIXES YOUR ERROR)
    profile, _ = Profile.objects.get_or_create(user=profile_user)

    posts = Post.objects.filter(user=profile_user)

    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'profile': profile,
        'posts': posts,
        'is_following': is_following,
        'followers_count': profile.get_followers_count(),
        'following_count': profile.get_following_count(),
        'posts_count': profile.get_posts_count(),
        'is_own_profile': request.user == profile_user,
    })


# ---------------- EDIT PROFILE ----------------
@login_required
def edit_profile(request):
    form = ProfileEditForm(request.POST or None, request.FILES or None, instance=request.user.profile)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile', username=request.user.username)

    return render(request, 'edit_profile.html', {'form': form})


# ---------------- COMMENT ----------------
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

    return redirect('home')


# ---------------- LIKE ----------------
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count()
    })


# ---------------- FOLLOW ----------------
@login_required
def toggle_follow(request, username):
    target_user = get_object_or_404(User, username=username)

    if target_user == request.user:
        return redirect('profile', username=username)

    follow, created = Follow.objects.get_or_create(
        follower=request.user,
        following=target_user
    )

    if not created:
        follow.delete()

    return redirect('profile', username=username)


# ---------------- SEARCH ----------------
def search_users(request):
    query = request.GET.get('q', '').strip()
    users = []

    if query:
        users = User.objects.filter(username__icontains=query)

        if request.user.is_authenticated:
            users = users.exclude(id=request.user.id)

        users = users[:10]

    return render(request, 'search.html', {
        'users': users,
        'query': query
    })