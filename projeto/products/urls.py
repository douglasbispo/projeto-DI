from django.urls import path
from . import views

urlpatterns = [
    path("cadastrar/", views.CreateView, name="create"),
    path("excluir/<int:id>", views.DeleteView, name="delete"),
    path("editar/<int:id>", views.EditView, name="edit"),
]
