from django.views.generic import CreateView, UpdateView

from .models import User


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
