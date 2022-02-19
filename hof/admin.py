from django.contrib import admin
from .models import Hof


class HofAdmin(admin.ModelAdmin):
    list_display = (
        'appearances',
        'goals',
        'assists',
        'titles',
    )


admin.site.register(Hof)
