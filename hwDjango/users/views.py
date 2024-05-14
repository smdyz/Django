# from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.core.mail import send_mail
import string
import random

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

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         if form.data.get('need_generate', False):
    #             self.object.set_password(
    #                 self.object.make_random_password(length=12)
    #             )
    #             self.object.save()
    #
    #     return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user


def recovery_password(request):
    context = {
        'success_message': 'Пароль успешно сброшен. Новый пароль был отправлен на ваш адрес электронной почты.',
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)

        characters = string.ascii_letters + string.digits
        characters_list = list(characters)
        random.shuffle(characters_list)
        password = ''.join(characters_list[:10])

        # user.set_password(make_password(password))
        user.set_password(password)
        user.save()

        send_mail(
            "Подтверждение регистрации",
            f"Добро пожаловать! Пароль успешно восстановлен. Новый пароль - {password}",
            "tima.zaplavnyy@ya.ru",
            [user.email],
            fail_silently=False,
        )

        return render(request, 'users/recover.html', context)

    return render(request, 'users/recover.html')

# class RecoverPasswordView(UpdateView):
#     model = User
#     form_class = UserRecoverPasswordForm
#     template_name = 'users/recover.html'
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         user = form.save(commit=False)
#         user_email = form.cleaned_data['email']
#         password = generate_random_password()
#         user.set_password(password)
#         user.save()
#         send_mail(
#             "Восстановление пароля",
#             f"Добро пожаловать! Ваш новый пароль - {password}",
#             "tima.zaplavnyy@ya.ru",
#             [user_email],
#             fail_silently=False,
#         )
#         print(user_email)
#         return response
