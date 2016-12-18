from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from ComicDatabase import views


def login_page(request):
    """A request to the login form
    :type request: HttpRequest
    """
    context = {'nav': views.nav(request)}

    if request.method == 'POST':
        post = request.POST
        username = post.get(key='username')
        password = post.get(key='password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            previous = request.GET.get(key='next')
            if previous is not None:
                return redirect(previous)
            else:
                return HttpResponseRedirect(redirect_to=reverse('ComicDatabase:index'))
    return render(request, 'ComicDatabase/login.html', context)


def logout_page(request):
    """
    Log out the currently logged in user
    :type request: HttpRequest
    """

    logout(request)

    return HttpResponseRedirect(reverse('ComicDatabase:index'))
