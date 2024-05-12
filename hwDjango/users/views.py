# from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail

from .forms import UserRegisterForm, UserProfileForm
from .models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user_email = form.cleaned_data['email']
        send_mail(
            "Подтверждение регистрации",
            "Добро пожаловать! Вы успешно зарегистрированы.",
            "tima.zaplavnyy@ya.ru",
            [user_email],
            fail_silently=False,
        )
        print(user_email)
        return response


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            if form.data.get('need_generate', False):
                self.object.set_password(
                    self.object.make_random_password(length=12)
                )
                self.object.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


class UserResetPassword:
    model = User






# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     success_url = reverse_lazy('catalog:store')
#
#
# class UserUpdateView(UpdateView):
#     model = User
#     form_class = UserForm
#     success_url = reverse_lazy('catalog:store')
