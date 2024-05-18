from django.contrib import admin
from .models import Task

# Register your models here.
## option one without decorator
# admin.site.register(Task)

# Option 2 Using the decorator
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'complete', 'Created')
