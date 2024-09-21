from django.contrib import admin
from .models import Room,Toppic,Message

# Register your models here.
admin.site.register(Room),
admin.site.register(Toppic),
admin.site.register(Message)