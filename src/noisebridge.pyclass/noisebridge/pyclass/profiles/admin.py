from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import UserProfile
from models import Interest

##removed for now
##class ProfileInline(admin.StackedInline):
##    model = UserProfile
##    fk_name = 'user'
##    max_num = 1
##
##
##class CustomUserAdmin(UserAdmin):
##    inlines = [ProfileInline,]
##
##
##admin.site.unregister(User)
##admin.site.register(User, CustomUserAdmin)


admin.site.register(UserProfile)
admin.site.register(Interest)
