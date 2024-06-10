from django.http import JsonResponse
from django.shortcuts import render
import mercadopago
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Preference
from .serializers import PreferenceSerializer


class PreferenceCreateView(APIView):

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

    def post(self, request, *args, **kwargs):
        serializer = PreferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f'serializerMP : {serializer}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Create your views here.
    

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