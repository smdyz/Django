from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


# UserCreationForm, UserChangeForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    # def clean_email(self):
    #     cleaned_data = self.cleaned_data['email']
    #
    #     if 'mail.ru' not in cleaned_data:
    #         raise forms.ValidationError('В поле должна быть указана почта mail.ru (например, example@mail.ru)')
    #
    #     return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'createable':
                field.widget.attrs['class'] = 'form-check-input'  # стиль для булевого поля (checkbox)


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'avatar', 'telephone_number', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'createable':
                field.widget.attrs['class'] = 'form-check-input'  # стиль для булевого поля (checkbox)

        self.fields['password'].widget = forms.HiddenInput()
