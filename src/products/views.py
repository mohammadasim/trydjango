from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    returned_product = {
        "object": product
    }
    return render(request, 'products/product_details.html', returned_product)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


def product_delete_view(request, product_id):
    product = get_object_or_404(Product, product_id)
    if request.method == "DELETE":
        product.delete()
        return redirect("../")