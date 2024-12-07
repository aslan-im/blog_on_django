from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    template_name = 'home.html'
    model = Post
    ordering = ['-created_at']

class ArticleDetailView(DetailView):
    template_name = 'post.html'
    model = Post

class AddPostView(CreateView):
    template_name = 'add_post.html'
    model = Post
    fields = '__all__'
    # fields = ('title', 'body')