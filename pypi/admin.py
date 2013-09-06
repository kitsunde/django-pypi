from django.contrib import admin
from pypi.models import Package


class PackageAdmin(admin.ModelAdmin):
    readonly_fields = Package._meta.get_all_field_names()
    has_add_permission = lambda s, r: False
    has_delete_permission = lambda s, r, o = None: False

    list_display = ('name', 'version', 'released_at')


admin.site.register(Package, PackageAdmin)
