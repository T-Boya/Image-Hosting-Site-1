from django.contrib import admin
from rango.models import Tag, Photo

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'url')

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields: {'slug':('name',)}

# admin.site.register(Photo, PageAdmin)
admin.site.register(Photo)
# admin.site.register(Tag, TagAdmin)
admin.site.register(Tag)