from django.contrib import admin

# Register your models here.

from .models import Room,Contact, Topic, Message,Notes

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Notes)
# admin.site.register(Contact)