from django.http import JsonResponse
from django.shortcuts import redirect, render
# SDK de Mercado Pago
import mercadopago

def home(request):
    return render(request, 'home.html')

def payment(request):
    return render(request, 'check_out_pro.html')


# Agrega credenciales
def checkout(request):
    sdk = mercadopago.SDK("APP_USR-3807241470267960-030922-93bb8ff68e2707c3c87882ca1021cdac-69661146")
    
    # Crea un ítem en la preferencia
    preference_data = {
        "items": [
            {
                "title": "Mi producto",
                "quantity": 1,
                "unit_price": 75.76,
            }
        ],
        "back_urls": {
            "success": "https://previ.com.ar/casos-de-exito/",
            "failure": "https://previ.com.ar/contacto/",
            "pending": "https://previ.com.ar/reingenieria-de-procesos/",
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    
    return JsonResponse({
        'id': preference['id']
    })