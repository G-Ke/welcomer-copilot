from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Organization, Domain

@admin.register(Organization)
class OrganizationAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'display_name', 'slug', 'main_contact_email', 'is_active', 'created_at')
    search_fields = ('name', 'display_name', 'slug', 'main_contact_email')
    list_filter = ('is_active', 'plan', 'on_trial')
    readonly_fields = ('uuid', 'created_at', 'updated_at')


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    pass