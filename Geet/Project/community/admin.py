from django.contrib import admin
from . models import Postmodel


# Register your models here.


@admin.register(Postmodel)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status')
    list_filter=('status','created_at','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    date_hierarchy='publish'
    raw_id_fields=('author',)
    ordering=('status','publish')