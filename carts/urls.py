from django.urls import path
from .views import *
from .serializers import *

urlpatterns = [
    path('carts', CartViews.as_view()),
]
