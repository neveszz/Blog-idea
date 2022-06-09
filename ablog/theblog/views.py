from django.shortcuts import render
from django.urls import reverse

from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
# def home(request):
#     return render(request, 'home.html',{}) -> old method


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    # ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'body', 'title_tag']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    def get_success_url(self):
        return reverse('home')


def CategoryView(request, catego):
    category_posts = Post.objects.filter(category=catego).order_by('-post_date')
    return render(request, 'categories.html', {'catego':catego.title(), 'category_posts':category_posts})