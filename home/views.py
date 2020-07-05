from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
from .forms import CreateUserForm

titulo = "Projetos Django"
subtitulo = "JCAVI"

def index(request):
    return render(request, 'home/index.html', { 'titulo': titulo, 'subtitulo': subtitulo})

def register(request):
    form = CreateUserForm()

    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            user = form.cleaned_data.get('username')
            messages.success(request, "A conta foi criada para " + user)
            return redirect('login_view')

    context = {'form':form, 'titulo': titulo, 'subtitulo': subtitulo}
    return render(request, 'home/register.html', context)

def login_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Nome de usuário e/ou senha está incorreto")

    context = {'form':form, 'titulo': titulo, 'subtitulo': subtitulo}
    return render(request, 'home/login.html', context)



def logout_view(request):
    logout(request)
    return render(request, 'home/logout.html', { 'titulo': titulo, 'subtitulo': subtitulo})
    # Redirect to a success page.