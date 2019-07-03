from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogapp:index'))


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    elif request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user_authenticated = authenticate(
                username=new_user.username,
                password=request.POST['password1'])
            login(request, user_authenticated)
            return HttpResponseRedirect(reverse('blogapp:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)

