from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from order.models import Product


class IndexView(View):
    def get(self, request):
        products = Product.objects.order_by("-created_at")[:3]
        return render(request, 'index.html', {"products": products})

class PaymentView(View):
    def get(self, request):
        return render(request, 'wallet/payment.html', { })

