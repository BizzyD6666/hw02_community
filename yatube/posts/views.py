from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    return render(request, template, {
        'posts': posts,
    })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    return render(request, 'posts/group_list.html', {
        'group': group,
        'posts': posts,
    })
