from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, NoteForm, LevelForm, SubjectForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Subject, Note



# Create your views here.
def index(request):
    return render(request,"index.html")


@login_required()
def home(request):
    return render(request, "home.html")


def blog(request):
    return render(request),"blog.html"


def register(request):
    if request.method == "POST":
        registerform = RegistrationForm(request.POST)
        if registerform.is_valid():
            user = registerform.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject= 'Activate your blog accout.'
            message = render_to_string('activate_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = registerform.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        registerform = RegistrationForm()
    return render(request,'register.html',{'registerform': registerform})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account')
    else:
        return HttpResponse('Activation link is invalid')

@login_required()
def addNote(request):
    if request.method == "POST" :
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
        return render(request, "notes.html",{'form':form})


def addSubject(request):
    if request.method == "POST" :
        form = SubjectForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()
        return render(request, "notes.html",{'form':form})


def addLevel(request):
    if request.method == "POST" :
        form = LevelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = LevelForm()
        return render(request, "notes.html",{'form':form})


def showNotes(request):
    notes = Note.objects.all()
    return render(request,"notes.html",{'note':notes})


def load_subject(request):
    level_id = request.GET.get('level')
    subject = Subject.objects.filter(level= level_id).order_by('document')
    return render(request,'notes.html',{'subject':subject})
