from django.contrib import admin
from crud.models import SoilUser
from crud.forms import UserForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from uuid import uuid4

@admin.register(SoilUser)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    ordering = ["username"]
    fields = ("username", "password", "user_type")
    list_display = ("username", "password", "user_type")
    list_display_links = ["username"]
    empty_value_display = "Campo descritivo não encontrado"

    actions = (
        "change_for_dealer",
        "change_for_user",
        "change_for_admin",
        "exclude_user",
    )
    
                  
    @admin.action(description="Excluir")
    def exclude_user(self, request, queryset):
        queryset.delete()

    @admin.action(description="Altere para Revendedor")
    def change_for_dealer(self, request, queryset):
        queryset.update(user_type="DEALER", is_superuser=False, is_staff=False, is_active=False)

    @admin.action(description="Altere para Usuário")
    def change_for_user(self, request, queryset):
        queryset.update(user_type="USER", is_superuser=False, is_staff=False, is_active=False)

    @admin.action(description="Altere para Administrador")
    def change_for_admin(self, request, queryset):
        queryset.update(user_type="SUDO", is_superuser=True, is_staff=True, is_active=True)
        
