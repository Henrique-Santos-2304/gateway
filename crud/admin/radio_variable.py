from django.contrib import admin
from crud.models import RadioVariables


@admin.register(RadioVariables)
class RadioVariablesAdmin(admin.ModelAdmin):
    ordering = ("pivot_id", "-id")
    fields = ("father", "rssi", "noise")
    list_display = ("pivot_id", "father", "rssi", "noise", "timestamp")
    list_display_links = ["pivot_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = ("father", "rssi", "noise")

    actions = ["exclude_radio_variable"]

    @admin.action(description="Excluir")
    def exclude_radio_variable(self, request, queryset):
        queryset.delete()
