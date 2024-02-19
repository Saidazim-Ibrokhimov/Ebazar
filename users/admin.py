from django.contrib import admin
from users.models import CustomeUser, Saved
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)
admin.site.register(CustomeUser)
admin.site.register(Saved)

