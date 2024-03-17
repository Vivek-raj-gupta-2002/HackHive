from django.shortcuts import render, HttpResponse, redirect
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
    new_data = dict()

    data = Group.objects.all().filter(name='helper')
    
    if len(data) != 0:
        req_data = User.objects.filter(groups=data)

        post = models.Post.objects.filter(is_anonymous=False)
        new_data = {'data': req_data[:3], 'top': req_data[3:7], 'post':post}
    
    return render(request, 'psyco.html', new_data)


def community(request):
    return render(request,'community.html')

@login_required
def dash(request):


    data = Group.objects.all().filter(name='helper')

    ans = dict()
    
    if len(data) != 0:
        
        req_data = User.objects.filter(groups=data[0])[2:5]

        ans['reco'] = req_data

    

    data_ = models.Diary.objects.filter(user=request.user)

    if request.method == 'POST':
        form = forms.diaryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()

    form = forms.diaryForm()
    ans['form'] = form
    ans['data'] = data_

    return render(request, 'dash.html', ans)


@login_required
def profile(request):
    
    """
    user models
    general server form
    rewards
    bestmates
    family members
    """
    my_user = User.objects.filter(username=request.user)[0]
    points = models.Rewards.objects.filter(user=request.user)

    if len(points) != 0:

        data = {
        'user' : request.user,
        'points': points.points,
        'email': my_user.email,
    }
        
    else:
        data = {
        'user' : request.user,
        
        'email': my_user.email,
    }

    return render(request, 'profile.html', data)

@login_required
def survey(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        

        return redirect('student_post')
    
    questions = [
"How would you rate your overall mood today?",
    "Have you been feeling anxious or stressed recently?",
    "Do you have trouble sleeping at night?",
    "Have you experienced changes in your appetite recently?",
    "Are you able to concentrate on tasks as usual?",
    "Do you often feel sad or hopeless?",
]


        
    return render(request,'survey.html', {'data': questions})

