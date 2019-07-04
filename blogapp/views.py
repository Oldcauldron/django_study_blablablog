from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from .models import Hashtag, Blogpost
from .forms import TagForm, PostForm

# Create your views here.


def index(request):
    return render(request, 'blogapp/index.html')


def check_owner(request, owner_tag_post):
    if owner_tag_post != request.user:
        raise Http404
    else:
        return True


def tags(request):
    tags = Hashtag.objects.all()
    req_user = request.user
    context = {'tags': tags, 'req_user': req_user}
    return render(request, 'blogapp/tags.html', context)


def tag(request, tag_id):
    hashtag = Hashtag.objects.get(id=tag_id)
    tag_page = hashtag.blogpost_set.order_by('date_added')
    context = {'hashtag': hashtag, 'tag_page': tag_page}
    return render(request, 'blogapp/tag.html', context)


def post(request, post_id):
    post = Blogpost.objects.get(id=post_id)
    req_user = request.user
    context = {'post': post, 'req_user': req_user}
    return render(request, 'blogapp/post.html', context)


def themes(request):
    requ = request.user
    if request.user.is_authenticated:
        themes = Blogpost.objects.filter(owner_post=requ).\
            order_by('date_added')
    else:
        themes = Blogpost.objects.order_by('date_added')
    context = {'themes': themes, 'req_user': requ}
    return render(request, 'blogapp/themes.html', context)


# def method_new(request, forma, revers, htmlfile):
#     '''создаем что то новое, тэг или пост'''
#     if request.method != 'POST':
#         form = forma()
#     elif request.method == 'POST':
#         form = forma(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse(revers))
#     context = {'form': form}
#     return render(request, htmlfile, context)


# @login_required
# def new_tag(request):
#     '''проба функции method_new сокращающей код'''
#     forma = TagForm
#     revers = 'blogapp:tags'
#     htmlfile = 'blogapp/new_tag.html'
#     return method_new(request, forma, revers, htmlfile)


@login_required
def new_tag(request):
    if request.method != 'POST':
        form = TagForm()
    elif request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save(commit=False)
            new_tag.owner_tag = request.user
            new_tag.save()
            return HttpResponseRedirect(reverse('blogapp:tags'))
    context = {'form': form}
    return render(request, 'blogapp/new_tag.html', context)


@login_required
def new_theme(request):
    if request.method != 'POST':
        form = PostForm()
    elif request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner_post = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogapp:themes'))
    context = {'form': form}
    return render(request, 'blogapp/new_theme.html', context)


@login_required
def edit_tag(request, tag_id):
    tag = Hashtag.objects.get(id=tag_id)
    check_owner(request, tag.owner_tag)
    if request.method != 'POST':
        form = TagForm(instance=tag)
    elif request.method == 'POST':
        form = TagForm(instance=tag, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogapp:tags'))
    context = {'form': form, 'tag': tag}
    return render(request, 'blogapp/edit_tag.html', context)


@login_required
def edit_post(request, post_id):
    post = Blogpost.objects.get(id=post_id)
    check_owner(request, post.owner_post)
    if request.method != 'POST':
        form = PostForm(instance=post)
    elif request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogapp:themes'))
    context = {'form': form, 'post': post}
    return render(request, 'blogapp/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    post = Blogpost.objects.get(id=post_id)
    check_owner(request, post.owner_post)
    post.delete()
    return HttpResponseRedirect(reverse('blogapp:themes'))


@login_required
def delete_tag(request, tag_id):
    tag = Hashtag.objects.get(id=tag_id)
    check_owner(request, tag.owner_tag)
    tag.delete()
    return HttpResponseRedirect(reverse('blogapp:tags'))
















