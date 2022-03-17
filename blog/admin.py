from django.contrib import admin
from .models import Post
from .models import Professor
from .models import Subject
from .models import Student

admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Student)

# Register your models here.
