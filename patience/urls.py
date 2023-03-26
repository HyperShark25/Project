from django.urls import path
from .views import Register, LoginView, LogoutView
from . import views


urlpatterns = [
    path('', Register.as_view(), name='create_profile'),
    path('login', LoginView.as_view(), name='login_profile'),
    path('mt', views.mohamedtemplate, name='mohamed')
    # path('logout', LogoutView.as_view(), name='logout')
]
