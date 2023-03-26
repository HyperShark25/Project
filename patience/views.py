from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import BlogForm
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class Login(LoginView):
    template_name = 'login_profile.html'
    # success_url = reverse_lazy('au')

    # def get_success_url(self):
    #     user = self.request.user
    #     if user.is_superuser:
    #         return reverse_lazy('/')
    #     else:
    #         return super().get_success_url()


# class Logout(LogoutView):
#     next_page = '/'

class Register(generic.CreateView):
    form_class = BlogForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('login_profile')


@login_required
def mohamedtemplate(request):
    return render(request, 'main_one.html')
