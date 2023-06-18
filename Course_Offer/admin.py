from django.contrib import admin
from .models import Course, Batch, Department, All
# Register your models here.

admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Department)
admin.site.register(All)
