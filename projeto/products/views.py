from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from .models import Product
from django.contrib import messages

# Create your views here.
@login_required
def CreateView(request):
    
    if(request.method == "POST"):
        form = ProductForm(request.POST, request.FILES)

        if(form.is_valid()):
            product = form.save(commit=False)
            product.save()

            messages.info(request, "Produto criado com sucesso!")

            return redirect("home")

    else: 
        form = ProductForm()

    return render(request, "create.html", {"form" : form})



@login_required
def DeleteView(request, id):

    product = get_object_or_404(Product, pk=id)
    product.delete()

    messages.info(request, 'Produto excluido com sucesso!')

    return redirect('dashboard')



@login_required
def EditView(request, id):

    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)

    if (request.method == "POST"):
        form = ProductForm(request.POST, request.FILES, instance=product)

        if (form.is_valid()):
            product.save()

            messages.info(request, 'Produto editado com sucesso!')

            return redirect('dashboard')
        else:
            return render(request, 'edit.html', {'form': form, 'product': product})

    else:
        return render(request, 'edit.html', {'form': form, 'product': product})