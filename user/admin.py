from django.contrib import admin

from .models import User  , Erreur,Client,Host

# Register your models here.

admin.site.register(User)
#admin.site.register(SuperAdmin)
admin.site.register(Erreur)
admin.site.register(Client)
admin.site.register(Host)
