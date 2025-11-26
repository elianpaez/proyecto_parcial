from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Alumno
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generar_pdf_alumno

class AlumnoDetailView(LoginRequiredMixin, DetailView):
    model = Alumno
    template_name = 'gestion/alumno_detail.html'

    def get_queryset(self):
        return Alumno.objects.filter(creado_por=self.request.user)




class DashboardView(LoginRequiredMixin, ListView):
    model = Alumno
    template_name = 'gestion/dashboard.html'
    context_object_name = 'alumnos'

    def get_queryset(self):
        return Alumno.objects.filter(creado_por=self.request.user).order_by('apellido')
    
class AlumnoCreateView(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = ['nombre', 'apellido', 'email'] 
    template_name = 'gestion/alumno_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)
    
@login_required
def enviar_pdf_por_correo(request, pk):
    
    alumno = get_object_or_404(Alumno, pk=pk, creado_por=request.user)

    
    pdf_data = generar_pdf_alumno(alumno)

    
    nombre_archivo = f"Reporte_{alumno.nombre}_{alumno.apellido}.pdf"

    email = EmailMessage(
        subject=f'Reporte de Alumno: {alumno.nombre} {alumno.apellido}',
        body=f'Adjunto encontrará el reporte oficial del alumno {alumno.nombre} {alumno.apellido}.',
        from_email=settings.EMAIL_HOST_USER, 
        to=['docente@tuuniversidad.com', request.user.email], 
    )

   
    email.attach(nombre_archivo, pdf_data, 'application/pdf')

    try:
        email.send()
        print(f"Correo enviado a {request.user.email} y docente.")
      
    except Exception as e:
        print(f"Error al enviar correo: {e}")
  

    return redirect('dashboard')