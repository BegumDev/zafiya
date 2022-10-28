from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout2, name='checkout2'),
    path('checkout_success2/<order_number>', views.checkout_success2, name='checkout_success2'),
]