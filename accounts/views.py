from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            send_mail(
                '¡Bienvenido a la Plataforma!',
                f'Hola {user.username},\nGracias por registrarte en nuestra plataforma.',
                settings.EMAIL_HOST_USER,  
                [user.email],              
                fail_silently=False,
            )

            return redirect('login')  
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
