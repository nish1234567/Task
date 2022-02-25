from django.urls import path,include
from .views import *

urlpatterns = [
    path('product/', ProductViews.as_view()),
    path('demo', ProductViews.as_view()),
]
