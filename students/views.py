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
    posts = models.Post.objects.filter()
    comments = models.Comments.objects.all()
    comm_form = models.Comments()

    # Save the form
    if request.method == 'POST':
        comm_form = models.Comments(request.POST)
        if comm_form.is_valid():
            comm_form = comm_form.save(commit=False)
            comm_form.user = user

            comm_form.save()

        comm_form = models.Comments()

    return HttpResponse('POST')


@login_required
def helpers(requests):
    """
    Get the helpers details
    Top and top 5
    """

    desired_group = Group.objects.get(name="Physicologist")
    
    posts = models.Post.objects.filter(is_anonymous=False)[:5]
    
    pass

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
