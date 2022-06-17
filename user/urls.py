from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.UserApiview.as_view()),
    path('login/', views.login_view.as_view()),
]