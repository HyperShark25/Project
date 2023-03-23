from django.contrib import admin
from .models import Device, New, LOD, Connection


class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'serial_number', 'date_created', 'option2', 'topic']


class NewAdmin(admin.ModelAdmin):
    list_display = ['id', 'secret_number', 'duration']


class LODAdmin(admin.ModelAdmin):
    list_display = ['id', 'option', 'option2']


class ConnectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'device']


admin.site.register(Device, DevicesAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(LOD, LODAdmin)
admin.site.register(Connection, ConnectionAdmin)
