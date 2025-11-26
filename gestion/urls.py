from django.urls import path

from .views import DashboardView, AlumnoCreateView, AlumnoDetailView, enviar_pdf_por_correo


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('crear/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('<int:pk>/enviar_pdf/', enviar_pdf_por_correo, name='enviar_pdf_por_correo'),
    path('<int:pk>/', AlumnoDetailView.as_view(), name='alumno_detail')
]