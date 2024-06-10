from django.http import JsonResponse
from django.shortcuts import redirect, render
# SDK de Mercado Pago
import mercadopago

def home(request):
    return render(request, 'home.html')

def payment(request):
    return render(request, 'check_out_pro.html')


# Agrega credenciales
