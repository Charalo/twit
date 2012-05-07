from django.contrib import admin
from main.models import Perfil, Twit


class TwitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'status', 'creacion',)


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario',  'cumple', 'ciudad', 'permisos', 'biografia',)


admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Twit, TwitAdmin)
