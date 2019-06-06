from django.urls import path
from todo.views import home_page

urlpatterns = [
    path('',home_page),
]