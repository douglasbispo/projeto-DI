from pyexpat import model
from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # colunas que irá mostrar na tabela
    list_display = ("name","description","quantity","price","validity","created_at","updated_at")

    # barra de pesquisa
    search_fields = ["name","description"]