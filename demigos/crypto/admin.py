from django.contrib import admin

from .models import Pair, PairRecord


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(PairRecord)
class PairRecordAdmin(admin.ModelAdmin):
    list_display = ('volume',)
