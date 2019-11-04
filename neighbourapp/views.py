from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .models import Neighbour,Police,Business
from django.contrib import messages
from .forms import CreateProfile,CreateNeighbour,UpdateProfile,UpdateNeighbour,UpdateUser,UserUpdate
from .email import send_welcome_email

# Create your views here.

def homePage(request):
    
    return render(request,'neighbour/homePage.html')

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


# def viewProfile(request):
#     if request.method=='POST':
        
#         profileForm=UpdateProfile(instance=request.user.profile)
#         # neighbourForm=UpdateNeighbour(instance=request.user.neighbour)
#         userForm=UpdateUser(request.POST,instance=request.user)
        

#         if userForm.is_valid() and profileForm.is_valid() and neighbourForm.is_valid():
#             userForm.save()
#             profileForm.save()
#             # neighbourForm.save()
            
#             messages.success(request,f' your account has been updated successfuly ')
#             return redirect('viewProfile')
#     else: 
#         userForm=UpdateUser(instance=request.user)
#         profileForm=UpdateProfile(instance=request.user.profile)
#         # neighbourForm=UpdateNeighbour(instance=request.user.neighbour)
        
#     context={
#         'uform':userForm,
#         'pform':profileForm,
#         # 'nform':neighbourForm
#         }
#     return render(request,'auth/profile.html',context)


def viewProfile(request):
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
        'nform': nform
    }

    return render(request, 'auth/profile.html', context)
