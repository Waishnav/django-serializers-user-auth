from django.contrib import admin

# add user model in admin
from . import models

class UserAdmin(admin.ModelAdmin):
  list_display = (
    "email",
    "first_name",
    "last_name",
    "id"
  )

admin.site.register(models.User, UserAdmin)
