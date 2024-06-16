from django.contrib import admin
from .models import Blog, Comment, Portfolio, Category, GetInTouch


admin.site.register(Blog)
admin.site.register(Portfolio)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(GetInTouch)
