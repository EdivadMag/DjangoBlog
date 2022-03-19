from django.contrib import admin
from .models import Post
from .models import Professor
from .models import Subject
from .models import Student
from .models import Rating

#admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Rating)

# Register your models here.
