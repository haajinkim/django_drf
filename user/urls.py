from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserApiview.as_view()),
    path('Join/', views.Join_Apiview.as_view()),
]