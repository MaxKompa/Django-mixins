from django.urls import path
from .views import MyView, AnotherView

urlpatterns = [
    path('user/<int:pk>/', MyView.as_view(), name='user_detail'),
    path('another/', AnotherView.as_view(), name='another_view'),
]
