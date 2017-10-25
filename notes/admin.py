from django.contrib import admin
from . models import Note, Category, Goal

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'body')

class GoalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Goal, GoalAdmin)
