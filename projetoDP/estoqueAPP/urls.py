from django.urls import path
from . import views

app_name = "estoque"

urlpatterns = [
    path("", views.home_app, name="home"),
    path("adicionar/", views.adicionar, name="adicionar"),
    path("remover/<int:id>", views.remover, name="remover"),
    path("editar/<int:id>", views.editar, name="editar"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
]
