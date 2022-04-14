from django.contrib import admin

from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    readonly_fields = ['title', 'price_without_disc', 'price_with_disc', 'brand', 'date']
