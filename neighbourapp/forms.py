from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserUpdate(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['profileImage','bio']

class UpdateUser(forms.ModelForm):
    class Meta:
        model=User
        fields=['username']


class CreateProfile(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['profileImage','bio']

class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=['postName','postText','postImage','postNeighbourName']

class CreateNeighbour(forms.ModelForm):
    class Meta:
        model=models.Neighbour
        fields=['neighbourLocation','neighbourName']

class UpdateNeighbour(forms.ModelForm):
    class Meta:
        model=models.Neighbour
        fields=['neighbourLocation','neighbourName']


