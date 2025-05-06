from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import EstoqueForm
from .models import EstoqueModel
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login


def home_app(request):
    contexto = {"nome": "Lucas", "estoque": EstoqueModel.objects.all()}
    return render(request, "estoque/home.html", context=contexto)


def adicionar(request: HttpRequest):
    if request.method == "POST":
        formulario = EstoqueForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("estoque:home")

    contexto = {"form": EstoqueForm}
    return render(request, "estoque/adicionar.html", context=contexto)


def remover(request: HttpRequest, id):
    produto = get_object_or_404(EstoqueModel, id=id)
    produto.delete()
    return redirect("estoque:home")


def editar(request: HttpRequest, id):
    produto = get_object_or_404(EstoqueModel, id=id)

    if request.method == "POST":
        formulario = EstoqueForm(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
            return redirect("estoque:home")

    formulario = EstoqueForm(instance=produto)
    context = {"form": formulario}
    return render(request, "estoque/editar.html", context=context)


def cadastro(request):
    if request.method == "GET":
        return render(request, "estoque/cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        pswd = request.POST.get("pswd")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Nome de usuário já está em uso.")

        if User.objects.filter(email=email).exists():
            return HttpResponse("E-mail já cadastrado.")

        criar_usuario = User.objects.create_user(
            username=username, email=email, password=pswd
        )
        criar_usuario.save()
        return HttpResponse("Usuário cadastrado com sucesso!")


def login(request):
    if request.method == "GET":
        return render(request, "estoque/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("pswd")

        user = authenticate(username=username, password=password)

        if user:
            django_login(request, user)
            return render(request, "estoque/home.html")
        else:
            return HttpResponse("Email ou senha invalido(s).")
