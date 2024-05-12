from django.forms import forms

from .models import User


# UserCreationForm, UserChangeForm, AuthenticationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'mail.ru' not in cleaned_data:
            raise forms.ValidationError('В поле должна быть указана почта mail.ru (например, example@mail.ru)')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'createable':
                field.widget.attrs['class'] = 'form-check-input'  # стиль для булевого поля (checkbox)
