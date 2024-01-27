from django.urls import path
from . import views

urlpatterns = [
    path('sendmessage/', views.SendMessage),
]
