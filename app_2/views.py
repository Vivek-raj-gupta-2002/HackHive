from django.shortcuts import render, HttpResponse
from . import forms, models
from students import forms, models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User



@login_required
def p_post(request):
    """
    Showing Posts
    Add anonumus posts
    seeing comments
    """

    user = User.objects.get(username=request.user.username)
    posts = models.Post.objects.all()
    post_form = forms.PostForm()

    # Save the form
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.user = user
            post_form.is_anonymous = False
            post_form.save()

        post_form = forms.PostForm()

    data = {
        'post': posts,
        'post_form': post_form
    }

    return render(request, 'p_post.html', data)

def p_schedule(request):


    return render(request,'p_schedule.html')

def p_earning(request):
    return render(request,'p_earning.html')

