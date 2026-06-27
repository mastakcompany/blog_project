from django.contrib import admin

from users_app.views import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio',
        'social_link',
    )
