from django.contrib import admin
from .models import Tests

@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    verbose_name = 'Test'
    list_display = ('testId', 'question', 'answer', 'score', 'tag', 'dateTime')
    list_filter = ('testId', 'question', 'answer', 'score', 'tag')
    search_fields = ('testId', 'question', 'answer', 'score', 'tag')
    ordering = ('testId', 'question', 'answer', 'score', 'tag')
    fields = ('testId', 'question', 'answer', 'score', 'tag')
    readonly_fields = ('testId', 'question', 'answer', 'score', 'tag')

    # delete selected
    actions = ['delete_selected']
    def delete_selected(self, request, queryset):
        queryset.delete()

    

# Register your models here.
