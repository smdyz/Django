from django import forms

from .models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'cost')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        desc_data = self.cleaned_data['description']
        ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in desc_data.split(' '):
            if word.lower() in ban_words:
                raise forms.ValidationError('В описании не должно быть запрещенных слов')

        return desc_data

    def clean_name(self):
        name_data = self.cleaned_data['name']
        ban_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in name_data.split(' '):
            if word.lower() in ban_words:
                raise forms.ValidationError('В названии не должно быть запрещенных слов')

        return name_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_name', 'version_num', 'sign')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'sign':
                field.widget.attrs['class'] = 'form-check-input'    # стиль для булевого поля (checkbox)
