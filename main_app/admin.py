from django.contrib import admin

from .models import Card


class CardAdmin(admin.ModelAdmin):
    read = ('title', 'price_without_disc', 'price_with_disc', 'brand', 'provider',)


admin.site.register(Card)
