from csv import field_size_limit
from email import header
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from flask_login import current_user
from .models import post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


"""def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'myapp/home.html', context)"""


class PostListView( ListView):
    model  = post
    template_name = 'myapp/home.html'
    context_object_name = 'posts'
    fields = ['title', 'content']
    ordering = ['-data_posted']
    paginate_by = 5

class PostUserView (ListView):
    model = post
    fields = ['title', 'content', 'auther']
    ordering = ['-data_posted']
    paginate_by = 5
    def get_queryset(self):
       "I don't get it how kwargs is working"
       myuser = get_object_or_404(User,id=self.kwargs.get('id'))
       print (myuser.id,"--------",self.kwargs.get('id'))
       return post.objects.filter(auther=myuser)

class PostDetailView(LoginRequiredMixin, DetailView):
    model  = post


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model  = post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.auther = self.request.user    
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.auther else  False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model  = post
    template_name_suffix = '_delete_form'
    success_url = '/'   
    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.auther else  False    

class PostCreateView(LoginRequiredMixin,CreateView):
    model  = post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.auther = self.request.user    
        return super().form_valid(form)


def about(request):
    return render(request, 'myapp/about.html', {'title': 'About'})

