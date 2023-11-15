from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogapp.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'blog_content',)
    success_url = reverse_lazy('blogapp:list')


class BlogListView(ListView):
    model = Blog
    success_url = reverse_lazy('mainapp:home')


class BlogDetailView(DetailView):
    model = Blog
    success_url = reverse_lazy('blogapp:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'blog_content', 'public_sign',)
    success_url = reverse_lazy('blogapp:list')

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogapp:list')