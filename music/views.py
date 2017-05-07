from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from .models import Album,Song,Comment,UserProfile
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views.generic import View
from .forms import User, UserForm
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name = "music/detail.html"

class Comments(generic.ListView):
    template_name = "music/comment.html"
    context_object_name = "all_comment"

    def get_queryset(self):
        return Comment.objects.all()

def favorite(request, id):
    selected_song=get_object_or_404(Song,pk=id)
    album=get_object_or_404(Album,id=selected_song.album.id)
    if(selected_song.is_favorite==True):
        selected_song.is_favorite=False
    else:
        selected_song.is_favorite=True
    selected_song.save()
    return render(request,"music/detail.html",{"album":album})

class AlbumCreate(CreateView):
    model = Album
    fields=["artist","album_title","genre","album_logo"]

class AlbumUpdate(UpdateView):
    model=Album
    fields = ["artist","album_title","genre","album_logo"]

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy("music:index")

class SongView(generic.ListView):
    template_name = "music/songlist.html"
    context_object_name = "all_songs"


    def get_queryset(self):
        return Song.objects.all()

def login_user(request):
    template_name="music/login.html"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "music/index.html")
            else:
                return render(request, template_name, {'error_message': 'Your account has been disabled'})
        else:
            return render(request,template_name, {'error_message': 'Invalid login'})
    return render(request, template_name)



def register(request):
    template_name = "music/registration_form.html"
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'music/index.html')
    context = {
        "form": form,
    }
    return render(request, template_name, context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)

class ProfileView(generic.DetailView):
    model = User
    slug_field = 'id'
    slug_url_kwarg = 'name'

    template_name = "music/profile.html"

def search_album(request):
    if request.method=="POST":
        search_text=request.POST['search']
    else:
        search_text=""
    album=Album.objects.filter(album_title__contains=search_text)
    return render(request,"music/search.html",{"albums":album,"search":search_text})

