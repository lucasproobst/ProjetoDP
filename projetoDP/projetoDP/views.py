from django.shortcuts import render


def home(request):
    return render(request, "estoque/main_home.html")