from django.contrib import admin
from django.urls import path, include 
from core.views import LoginView, SignupView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('', include('product.urls')),
]
