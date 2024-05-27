from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import login
from .forms import UserRegisterForm, ProfileForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.forms import forms
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido creado exitosamente')
            return redirect('home')
        else:
            messages.warning(request, 'La creacion de usuario ha tenido un problema.')

    else:
        form = UserRegisterForm()
        
    context = { 
        'form' : form,
        'title': 'Registrarse',
        'Action': 'create',
    }

    return render(request, 'register.html', context)



class LoginFormView(LoginView):
    template_name = 'login.html'
    

    def get_context_data(self, **kwargs):
          
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        context['entity'] = 'Ingreso'
        context['list_url'] = reverse_lazy('home')
        context['action'] = 'login'

        return context
    


class LogoutFormView(LogoutView):
    template_name = 'logout.html'

    def get_context_data(self, **kwargs):
          
          context = super().get_context_data(**kwargs)
          context['title'] = 'Logout'
          context['entity'] = 'Salida'
          context['list_url'] = reverse_lazy('login')
          context['action'] = 'logout'
            
          return context

        
@login_required
def profile_view(request, username):
    if username is not None:

        user = CustomUser.objects.get(username=username)
        if request.method == 'POST':
            
            profile_form = ProfileForm(request.POST, request.FILES, instance=user)
            if profile_form.is_valid():
                profile_form.save()
                message = 'Cambios guardados correctamente'
                messages.success(request, message)
            else:
                message= 'Hubo un error al registrar los cambios'
                messages.error(request, message)
                
            
        else:
            profile_form = ProfileForm(instance=user)

        context = {
            'user_profile': user,
            'profile_form': profile_form,
        }

        return render(request, 'profile.html', context)
    return render(request, 'login.html')



class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    success_message = "Se ha enviado un correo electrónico con instrucciones para restablecer la contraseña."
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'  # Cambia esto a la plantilla que estás utilizando
    form_class = SetPasswordForm  # Especifica el formulario que deseas utilizar


