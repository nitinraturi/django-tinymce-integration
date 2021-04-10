from django.contrib import admin
from .models import *
from .forms import *


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(Blog, BlogAdmin)
