from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.UserApiview.as_view()),
]