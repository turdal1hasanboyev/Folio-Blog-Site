from django.contrib import admin
from .models import Blog, Comment, Portfolio


admin.site.register(Blog)
admin.site.register(Portfolio)
admin.site.register(Comment)
