from collections import defaultdict
from math import ceil
from os.path import join

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from django.utils import timezone
from .models import Post

exclude_posts = ("about", "projects", "talks")


def handler404(request):
    return render(request, 'blog/404.html', status=404)


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# def home(request, page=''):
#     args = dict()
#     args['blogposts'] = Post.objects.exclude(title__in=exclude_posts)
#     max_page = ceil(len(args['blogposts']) / 3)
#     if page and int(page) < 2:  # /0, /1 -> /
#         return redirect("/")
#     else:
#         page = int(page) if (page and int(page) > 0) else 1
#         args['page'] = page
#         args['prev_page'] = page + 1 if page < max_page else None
#         args['newer_page'] = page - 1 if page > 1 else None
#         # as template slice filter, syntax: list|slice:"start:end"
#         args['sl'] = str(3 * (page - 1)) + ':' + str(3 * (page - 1) + 3)
#         return render(request, 'blog/post_list.html', args)
#
#
# def about(request):
#     the_about_post = get_object_or_404(Post, title="about")
#     args = {"about": the_about_post}
#     return render(request, 'blog/about.html', args)
#
#
# def projects(request):
#     # use markdown to show projects
#     the_projects_post = get_object_or_404(Post, title="projects")
#     args = {"projects": the_projects_post}
#     return render(request, 'blog/projects.html', args)
#
#
# def talks(request):
#     # use markdown to show talks, could be changed if need better formatting
#     the_talks_post = get_object_or_404(Post, title="talks")
#     args = {"talks": the_talks_post}
#     return render(request, 'blog/talks.html', args)
