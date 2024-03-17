from django.shortcuts import render, HttpResponse
from . import forms, models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User


"""
STUDENTS PORTAL

"""

@login_required
def post(request):
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

            post_form.save()

        post_form = forms.PostForm()

    data = {
        'post': posts,
        'post_form': post_form
    }

    return render(request, 'post.html', data)


@login_required
def helpers(request):
    """
    Get the helpers details
    Top and top 5
    """

    data = Group.objects.all().filter(name='helper')[0]
    
    req_data = User.objects.filter(groups=data)

    post = posts = models.Post.objects.filter(is_anonymous=False)
    
    
    return render(request, 'psyco.html', {'data': req_data[:3], 'top': req_data[3:7], 'post':post})

def community(request):
    return render(request,'community.html')

@login_required
def dash(request):
    

    return render(request, 'dash.html')


@login_required
def profile(requests):
    
    """
    user models
    general server form
    rewards
    bestmates
    family members
    """
    pass



