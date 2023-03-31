from django.contrib import admin

# Register your models here.

from .models import Room,Contact, Topic, Message,Notes,Student,Chat

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Notes)
admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Chat)