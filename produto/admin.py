from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from produto.models import Categoria, Produto


admin.site.register(Categoria)

admin.site.register(Produto)
