from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blogapp.models import Blog
from pytils.translit import slugify


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'blog_content',)
    success_url = reverse_lazy('blogapp:list')


    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    success_url = reverse_lazy('mainapp:home')

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        # queryset = queryset.filter(public_sign=True)
        return queryset



class BlogDetailView(DetailView):
    model = Blog
    success_url = reverse_lazy('blogapp:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views +=1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'blog_content', 'public_sign',)
    success_url = reverse_lazy('blogapp:list')


    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()

        return super().form_valid(form)


    def get_success_url(self):
        return reverse('blogapp:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogapp:list')


def toggle_publish(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.public_sign:
        blog_item.public_sign = False
    else:
        blog_item.public_sign = True

    blog_item.save()

    return redirect(reverse('blogapp:list'))
