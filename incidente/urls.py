from django.urls import path
from incidente.views import incidentes,crear_incidente, detalle_incidente


urlpatterns = [
    
path( '',incidentes,name="Incidentes"),
    path('crear-incidente/', crear_incidente, name='crear_incidente'),
    path('detalle-incidente/<int:pk>/', detalle_incidente, name='detalle_incidente'),

]