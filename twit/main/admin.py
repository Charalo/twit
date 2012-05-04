from django.contrib import admin
from main.models import perfil, twit


class twitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'status', 'creacion',)


class perfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imagen_perfil', 'cumple', 'ciudad', 'permisos', 'biografia',)


admin.site.register(perfil, perfilAdmin)
admin.site.register(twit, twitAdmin)
