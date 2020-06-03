from django.contrib import admin
from .models import Cliente, Endereco, Telefone

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Telefone)
