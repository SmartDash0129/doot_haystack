from django.urls import path
from .views import test_func

urlpatterns = [
    path('test', test_func, name="test"),
]