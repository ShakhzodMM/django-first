from django.contrib import admin
from .models import CustomUser, Saved
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)  # Django admin panelida Group modelini ro'yxatdan chiqarish
admin.site.register(CustomUser)
admin.site.register(Saved)