from django.contrib import admin
from crud.models import Farm


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    ordering = ["farm_name"]
    exclude = ["farm_id"]

    list_display = (
        "id",
        "farm_id",
        "farm_name",
        "farm_city",
        "farm_lat",
        "farm_lng",
        "dealer",
    )

    list_display_links = ["id", "farm_id"]
    empty_value_display = "Campo descritivo não encontrado"
    list_editable = (
        "farm_name",
        "farm_city",
        "farm_lat",
        "farm_lng",
        "dealer",
    )

    actions = ["exclude_farm"]

    @admin.action(description="Excluir")
    def exclude_farm(self, request, queryset):
        queryset.delete()
