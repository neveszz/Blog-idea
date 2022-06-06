from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# def home(request):
#     return render(request, 'home.html',{}) -> old method


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
