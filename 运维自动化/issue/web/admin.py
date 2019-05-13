from django.contrib import admin
from .models import UserProfile
from .user_forms import UserCreateForm


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    form = UserCreateForm


admin.site.register(UserProfile, UserAdmin)
