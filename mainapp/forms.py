from django import forms
from mainapp.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'category', 'picture', 'price',)
        # excude = ('is_active',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for obj in prohibited_list:
            if obj in cleaned_data:
                raise forms.ValidationError("Продукт запрещен на площадке")

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'name', 'number_version', 'current_version',)
