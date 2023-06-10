from django.db import models

class Incidente(models.Model):
    ESTADOS = (
        ('EN_PROCESO', 'En proceso'),
        ('NUEVO', 'Nuevo'),
        ('ACCION_CLIENTE', 'Acción de cliente'),
        ('ESCALADO_SAP', 'Escalado a SAP'),
        ('RESUELTO', 'Resuelto'),
    )

    PRIORIDADES = (
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    reportado_por = models.CharField(max_length=255)
    consultor = models.CharField(max_length=255)
    estado = models.CharField(max_length=50, choices=ESTADOS)
    prioridad = models.CharField(max_length=50, choices=PRIORIDADES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    seccion_texto = models.TextField()
    adjunto = models.FileField(upload_to='adjuntos/', blank=True)

    def __str__(self):
        return self.titulo

