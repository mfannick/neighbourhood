from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Neighbour,Police,Business,Post
from django.contrib import messages
from .forms import CreateProfile,CreateNeighbour,UpdateProfile,UpdateNeighbour,UpdateUser,UserUpdate,PostForm
from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/')
def homePage(request):
    posts=Post.objects.all()
    user=request.user
    return render(request,'neighbour/homePage.html' ,{'posts':posts, 'user':user})

def signUp(request):
    currentUser=request.user
    if request.method=='POST':
        form=UserUpdate(request.POST)
        pform=CreateProfile(request.POST)
        nform=CreateNeighbour(request.POST)
        if form.is_valid() and pform.is_valid() and nform.is_valid():
            user=form.save()
            
            #profile
            profile=pform.save(commit=False)
            profile.user=user
            profile=pform.save()
            #neighbour
            neighbour=nform.save(commit=False)
            neighbour.user=user
            neighbour=nform.save()

            username=form.cleaned_data.get('username')
          
            messages.success(request,f'{username} , your account was successfuly created')
            return redirect('logIn')
    else:
        form=UserUpdate()
        pform=CreateProfile()
        nform=CreateNeighbour()

       
    return render(request,'auth/signUp.html',{
            'form':form ,
            'pform':pform,
            'nform':nform
        })

def logIn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homePage')
    else:
        form=AuthenticationForm()
    return render(request,'auth/logIn.html',{'form':form})

def logOut(request):
    if request.method=='POST':
        logout(request)
        return redirect('logIn')
    return redirect('logIn')

@login_required(login_url='/')
def viewProfile(request):
    posts=Post.objects.filter(user__username=request.user.username)
    if request.method == 'POST':
        uform = UpdateUser(request.POST, instance=request.user)
        pform = UpdateProfile(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        nform = UpdateNeighbour(request.POST,
                                   request.FILES,
                                   instance=request.user.neighbour)
        if uform.is_valid() and pform.is_valid() and nform.is_valid():
            uform.save()
            pform.save()
            nform.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('viewProfile')

    else:
        uform = UpdateUser(instance=request.user)
        pform = UpdateProfile(instance=request.user.profile)
        nform = UpdateNeighbour(instance=request.user.neighbour)

    context = {
        'uform': uform,
        'pform': pform,
        'nform': nform,
        'posts':posts,
    }

    return render(request, 'auth/profile.html', context)




@login_required(login_url='/')
def post(request):
    current_user = request.user
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homePage' )
    else:
        form=PostForm()
    return render(request,'neighbour/post.html',{'form':form})




