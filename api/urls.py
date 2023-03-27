from django.urls import path
from .views import DeviceView, ConnectionView, DeviceUpdateView, DeviceViewForm, RegisterView, LoginUser, LogoutUser
from . import views


urlpatterns = [
    path('api', DeviceView.as_view(), name='api'),     # path('api/', views.DeviceView.as_view(), name='api_view')
    # path('api/token/', obtain_auth_token, name='obtain'),
    path('', views.dragon, name='dragon'),
    path('<int:pk>', views.second, name='second'),
#    path('hello', MainViewClass.as_view()),
#     path('register', views.register, name='register'),
    path('register', RegisterView.as_view(), name='register'),
    # path('login/', views.login, name='login'),
    path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', views.logout, name='logout'),
    path('logout/', LogoutUser.as_view(), name='logout'),
#    path('hello', views.myform, name='hello'),
    path('hello', DeviceViewForm.as_view(), name='hello'),
    path('lod', views.like, name='like'),
    path('api2', ConnectionView.as_view()),
    path('<int:pk>/hello2/', DeviceUpdateView.as_view(), name='hello2')
]
