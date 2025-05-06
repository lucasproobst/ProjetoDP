from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home,),
    path(
        "estoque/", include("estoqueAPP.urls")
    ),  # Agrupamento de rotas usando o include
]
