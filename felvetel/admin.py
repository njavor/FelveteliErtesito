from django.contrib import admin
from .models import Jelentkezo, Tagozat

class JelentkezoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Információk', {
            'fields': ('nev', 'azonosito'),
        }),
        ('Pontok', {
            'fields': ('A', 'B', 'C1', 'C2', 'D1', 'D2', 'E', 'F1', 'F2'),
            'classes': ('collapse',),
        }),
        ('Felvétel eredménye', {
            'fields': (('tagozatok','felveve',)),
        })
    )

admin.site.register(Tagozat)
admin.site.register(Jelentkezo, JelentkezoAdmin)