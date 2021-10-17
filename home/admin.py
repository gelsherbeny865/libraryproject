from django.contrib import admin
from home.models import createbook ,student,BookInstance


# Register your models here.


admin.site.register(createbook)

admin.site.register(student)
admin.site.register(BookInstance)