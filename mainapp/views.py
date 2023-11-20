from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mainapp.forms import ProductForm, VersionForm
from mainapp.models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'picture', 'price',)
    # template_name = 'mainapp/product_form.html'
    success_url = reverse_lazy('mainapp:list')

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
        try:
            self.object.owner = self.request.user
        except ValueError:
            return redirect(reverse('usersapp:login'))

        else:
            formset = self.get_context_data()['formset']
            self.object = form.save()
            self.object.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
                return super().form_valid(form)




class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('mainapp:list')


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
        try:
            self.object.owner = self.request.user
        except ValueError:
            return redirect(reverse('usersapp:login'))

        else:
            formset = self.get_context_data()['formset']
            self.object = form.save()
            self.object.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
                return super().form_valid(form)



class ProductListView(ListView):
    model = Product
    form_clss = ProductForm
    # template_name = 'mainapp/product_list.html'
    success_url = reverse_lazy('mainapp:list')


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            # print(product)
            # print(context)
            active_version = product.version_set.filter(current_version=True).first()
            # print(active_version)
            if active_version:
                product.active_version_number = active_version.number_version
                product.active_version_name = active_version.name
                # print(product.active_version_number)
                # print(product.active_version_name)
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context



# def products(request):
#     products_list = Product.objects.all()
#     context = {
#         'objects_list': products_list,
#         'title': 'Каталог продуктов'
#     }
#     return render(request, 'mainapp/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/product_detail.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        product = context['object']

        active_version = product.version_set.filter(current_version=True).last()
        if active_version:
            product.active_version_number = active_version.number_version
            product.active_version_name = active_version.name
        else:
            product.active_version_number = None
            product.active_version_name = None

        return context


# def product(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'О товаре'
#     }
#     return render(request, 'mainapp/product_detail.html', context)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('mainapp:list')

    def get_success_url(self):
        if self.request.user == 'AnonymousUser':
            self.object.save()
            return reverse('mainapp:list')

        return reverse('usersapp:login')




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


