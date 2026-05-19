from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'your@email.com'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Choose a username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Confirm password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Password'
    }))


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': "What's on your mind?",
            'rows': 4
        }),
        max_length=2000
    )
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'file-input',
        'accept': 'image/*'
    }))

    class Meta:
        model = Post
        fields = ['content', 'image']


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'comment-input',
            'placeholder': 'Write a comment...'
        }),
        max_length=500
    )

    class Meta:
        model = Comment
        fields = ['text']


class ProfileEditForm(forms.ModelForm):
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': 'Tell people about yourself...',
            'rows': 3
        }),
        max_length=300
    )
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'file-input',
        'accept': 'image/*'
    }))

    class Meta:
        model = Profile
        fields = ['bio', 'profile_image']
