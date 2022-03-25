from django.contrib import admin
from .models import CustomUser,Team, Task
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model= CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User_role',
            {
                'fields':(
                    'Team_member',
                    'Team_leader',
                    'Availability',
                )
            }
        )
    )


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Team)
admin.site.register(Task)