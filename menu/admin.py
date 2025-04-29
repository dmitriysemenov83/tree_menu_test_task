from django.contrib import admin
from menu.models import Menu, MenuItem

admin.site.site_header = 'Панель управления'
admin.site.index_title = 'Администрирование'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent')
    list_filter = ('menu',)
    search_fields = ('title',)