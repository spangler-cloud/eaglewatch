from django.contrib import admin
from .models import Post
from datetime import date

class PostAdmin(admin.ModelAdmin):
    list_display = ('species', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['species', 'details']
    prepopulated_fields = {'slug': ('species','sequence','upload_Date')}

admin.site.register(Post, PostAdmin)