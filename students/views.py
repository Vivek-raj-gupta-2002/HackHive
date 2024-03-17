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

    data = Group.objects.all().filter(name='helper')[0]
    
    req_data = User.objects.filter(groups=data)

    post = models.Post.objects.filter(is_anonymous=False)
    
    
    return render(request, 'psyco.html', {'data': req_data[:3], 'top': req_data[3:7], 'post':post})


def community(request):
    return render(request,'community.html')

@login_required
def dash(request):


    data = Group.objects.all().filter(name='helper')[0]
    
    req_data = User.objects.filter(groups=data)[2:5]

    

    data_ = models.Diary.objects.filter(user=request.user)

    if request.method == 'POST':
        form = forms.diaryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user

            form.save()

    form = forms.diaryForm()


    data = {'reco': req_data, 'form': form, 'data': data_}

    return render(request, 'dash.html', data)


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
    points = models.Rewards.objects.filter(user=request.user)[0]


    data = {
        'user' : request.user,
        'points': points.points,
        'email': my_user.email,
    }

    return render(request, 'profile.html', data)

@login_required
def survey(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        

        return redirect('student_post')
    
    questions = [
    "Do you have antigen A in your blood?",
    "Do you have antigen B in your blood?",
    "Do you have both antigens A and B in your blood?",
    "Do you have the Rh factor in your blood?",
    "What is your blood type?"
]


        
    return render(request,'survey.html', {'data': questions})

