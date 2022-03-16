from django.contrib import admin
from .models import Post
from .models import Professor
from .models import Subject

admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Subject)

# Register your models here.
