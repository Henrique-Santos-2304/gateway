from django.contrib import admin
from crud.models import StateVariables


@admin.register(StateVariables)
class StateVariablesAdmin(admin.ModelAdmin):
    ordering = ("state_id", "-id")
    fields = ("angle", "percentimeter")
    list_display = ("state_id", "angle", "percentimeter")
    list_display_links = ["state_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = ("angle", "percentimeter")
    actions = ["exclude_state_variable"]

    @admin.action(description="Excluir")
    def exclude_state_variable(self, request, queryset):
        queryset.delete()
