from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

from map.utils import DataMixin

from .forms import *


  
from .models import Category, Heh

def map_home(request):
    recept = Heh.objects.all
    cats = Category.objects.all
    return render(request, 'map/map_home.html', {'recept': recept, 'cats': cats, 'cat_selected': 0,})

def show_post(request, post_id):
    post = get_object_or_404(Heh, pk=post_id)
    return render(request, 'map/post.html', {'post': post, 'cat_selected': post.cat_id,})

def show_category(request, cat_id):
    recept = Heh.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    return render(request, 'map/map_home.html', {'recept': recept, 'cats': cats, 'cat_selected': cat_id,})

def addrecept(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('map_home')
    else:
        form = AddPostForm()
    return render(request, 'map/addrecept.html', {'form': form})

#def login(request):
    #return HttpResponse("logn")

#def register(request):
    #return HttpResponse("register")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'map/register.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация") 
        return dict(list(context.items()) + list(c_def.items()))
    
class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'map/login.html'

    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация") 
        return dict(list(context.items()) + list(c_def.items()))   
    
    def get_success_url(self):
        return reverse_lazy('map_home')
    
    
def logout_user(request):
    logout(request)
    return redirect('login')

