from django.shortcuts import render

from django.views.generic import ListView
from user.models import Post


def home(request):
    return render(request, 'blog/home.html')


class Home(ListView):
    model = Post

    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_published']
    queryset = Post.objects.filter(
        date_published__isnull=False)
