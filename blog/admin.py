from django.contrib import admin
from .models import Post
# Register your models here.
# class BlogSlug(admin.ModelAdmin):
#     list_display = ("title"," ")
#     prepopulated_fields = {"slug": ("title","")}  
  
admin.site.register(Post)