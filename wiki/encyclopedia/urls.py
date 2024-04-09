from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:titulo>", views.entrada, name="entrada"),
    path("busqueda/", views.busqueda, name="busqueda"),
    path("agregar/", views.agregar, name="agregar"),
    path("ramdon/", views.ramdon_entrada, name="random"),
    path("editar/<str:titulo>", views.editar, name="editar"),
    

]