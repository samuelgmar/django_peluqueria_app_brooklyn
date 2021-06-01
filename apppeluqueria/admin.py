from django.contrib import admin
from .models import cliente, direccion, categoria,servicio, jefe, trabajador, reserva, hora, fecha, fechaTrabajador, galeria
from django.contrib.auth.models import Permission
# Register your models here.
admin.site.register(cliente)
admin.site.register(direccion)
admin.site.register(Permission)
admin.site.register(categoria)
admin.site.register(servicio)
admin.site.register(jefe)
admin.site.register(trabajador)
admin.site.register(reserva)
admin.site.register(hora)
admin.site.register(fecha)
admin.site.register(fechaTrabajador)
admin.site.register(galeria)

