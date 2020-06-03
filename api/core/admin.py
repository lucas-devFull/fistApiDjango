from django.contrib import admin
from .models import Cliente
from .models import Endereco

admin.site.register(Cliente)
admin.site.register(Endereco)
