from django.shortcuts import render, redirect
from .serializers import DeviceSerializer, ConnectionSerializer
from .models import Device, LOD, Connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import DeviceForm, UserRegisterForm
from rest_framework import generics
from django.urls import reverse_lazy


class DeviceView(APIView):

    def get(self, request, *args, **kwargs):
        item = Device.objects.all()
        serializer = DeviceSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ConnectionView(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


@login_required
def second(request, pk):
    a = Device.objects.get(id=pk)
    return render(request, 'second.html', {'a': a})


def dragon(request):
    a = Device.objects.all()
    return render(request, 'dragon.html', {'a': a})


def like(request):
    item = LOD.objects.all()
    return render(request, 'lod.html', {'item': item})


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    template_name = 'login.html'


class LogoutUser(LogoutView):
    next_page = '/'


@method_decorator(login_required, name='get')
class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = 'hello2.html'
    success_url = '/'


# def myform(request):
#     if request.method == 'POST':
#         form = DeviceForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
#     else:
#         form = DeviceForm()
#     return render(request, 'hello.html', {'form': form})

@method_decorator(login_required, name='get')
class DeviceViewForm(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'hello.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)
