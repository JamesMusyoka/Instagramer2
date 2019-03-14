from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
from django.http  import HttpResponse
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required


def index(request):
    images = []
    images = Image.get_images() 
    print(images)

    return render(request,'index.html',{'images': images})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
        return render(request,'registration/success.html')
        
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def profile(request):
    # profiles = Profile.search_profile()
    print(profile)
    return render(request,'profile/profile.html')

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})

def like(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    request.user.profile.like(image)
    return JsonResponse(image.imagelikes.count(), safe=False)

def single_image(request, image_id):
    image = Image.get_image_id(image_id)
    comments = Comments.get_comments_by_images(image_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return redirect('single_image', image_id=image_id)
    else:
        form = CommentForm()

    return render(request, 'image.html', {'image':image, 'form':form, 'comments':comments})


