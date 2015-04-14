from django.contrib import admin
from resumes.models import User, Tag


class TagInLine(admin.StackedInline):
    model = Tag
    extra = 5

class UserAdmin(admin.ModelAdmin):
    inlines = [TagInLine]

admin.site.register(User, UserAdmin)