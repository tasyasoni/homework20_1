from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from mainapp.forms import ProductForm, VersionForm
from mainapp.models import Product, Version





class ProductCreateView(CreateView):
    model = Product
    form_clss = ProductForm
    fields = ('name', 'description', 'category', 'picture', 'price',)
    # template_name = 'mainapp/product_form.html'
    success_url = reverse_lazy('mainapp:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form = VersionForm, extra =1)
        if self.request.method =='POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance = self.object )
        else:
            context_data['formset'] = SubjectFormset(instance = self.object)
        return context_data


    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    form_clss = ProductForm
    template_name = 'mainapp/products.html'
    success_url = reverse_lazy('mainapp:products')


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
