from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mainapp.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'


# def products(request):
#     products_list = Product.objects.all()
#     context = {
#         'objects_list': products_list,
#         'title': 'Каталог продуктов'
#     }
#     return render(request, 'mainapp/products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/product.html'

# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'О товаре'
#     }
#     return render(request, 'mainapp/product.html', context)

def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Все получилось contacts: {name} {phone}: {message}')

    return render(request, 'mainapp/contacts.html', context)


def home(request):
    context = {
        'title': 'Product_store'
    }
    return render(request, 'mainapp/home.html', context)
