from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("payment/", views.PaymentView.as_view(), name='payment')
]
