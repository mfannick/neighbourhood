from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfile,UpdateUser,ProjectForm,CreateProfile,CommentForm,UserRegistrationForm
from .models import Profile,Project,Comment
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404,JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# "token": "f32dbfb4e7b32dd468268991c1872a91d50f6891"

#serializing

############# project model

class ProjectList(APIView):
    def get(self, request, format=None):
        allProjects = Project.objects.all()
        serializers = ProjectSerializer(allProjects, many=True)
        return Response(serializers.data)

        def post(self, request, format=None):
            serializers = ProjectSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            permission_classes = (IsAdminOrReadOnly,)



class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def getProject(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.getProject(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.getProject(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        project = self.getProject(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############# profile model

class ProfileList(APIView):
    def get(self, request, format=None):
        allProfiles = Profile.objects.all()
        serializers = ProfileSerializer(allProfiles, many=True)
        return Response(serializers.data)

        def post(self, request, format=None):
            serializers = ProfileSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            permission_classes = (IsAdminOrReadOnly,)



class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def getProfile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.getProfile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.getProfile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        profile = self.getProfile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# Create your views here.
def homePage(request):
    projects=Project.objects.all()
    return render(request,'project/homePage.html',{'projects':projects})

def signUp(request):
    currentUser=request.user
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        pform=CreateProfile(request.POST)
        if form.is_valid() and pform.is_valid():
            user=form.save()
            profile=pform.save(commit=False)
            profile.user=user
            profile=pform.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} , your account was successfuly created')
            return redirect('logIn')
    else:
        form=UserCreationForm()
        pform=CreateProfile()
    return render(request,'auth/signUp.html',{'form':form ,'pform':pform})

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
        return redirect('homePage')




@login_required(login_url='/login/')
def viewProfile(request):
    if request.method=='POST':
        
        profileForm=UpdateProfile(instance=request.user.profile)
        userForm=UpdateUser(request.POST,instance=request.user)
        

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            
            messages.success(request,f' your account has been updated successfuly ')
            return redirect('viewProfile')
    else: 
        userForm=UpdateUser(instance=request.user)
        profileForm=UpdateProfile(instance=request.user.profile)
        

    return render(request,'auth/profile.html',{'uform':userForm,'pform':profileForm})


@login_required(login_url='/login/')
def postProject(request):
    current_user = request.user
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.userF=current_user
            project.save()

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homePage' )
    else:
        form=ProjectForm()
    return render(request,'project/postProject.html',{'form':form})



def projectDetails(request,project_id):
    # comments=Comment.objects.get(id=commentId)
    project = Project.objects.get(id = project_id)
    # comments=Comment.objects.filter(comment=currentUser)  
    return render(request,"project/projectDetails.html", {'project':project})

@login_required(login_url='/login/')
def searchProject(request):
    if 'project' in request.GET and request.GET['project']:
        search_term=request.GET.get('project')
        projects=Project.searchProjects(search_term)
        message = f"{search_term}"

        return render(request,'project/search.html',{'message':message,'projects':projects})
    else:
        message='no search yet'
        return render(request,'project/search.html',{'message':message})

# @login_required(login_url='/login/')
# def comment(request):
#     form=CommentForm
    
#     if request.is_ajax():
#         form=CommentForm(request.POST)
#         if form.is_valid():
#             instance=form.save(commit=False)
#             instance.user=request.user
#             instance.save()
#             data={
#                 'message':'project comment',
#             }
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return JsonResponse(data) 
#     else:
#         form=CommentForm()

#     return render(request,'project/comment.html',{'form':form})



        


