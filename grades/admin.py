from django.contrib import admin

from .models import Student, Lesson, Grade


class GradeInline(admin.TabularInline):
    model = Grade
    extra = 0


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [GradeInline]


admin.site.register(Student)
admin.site.register(Lesson, LessonAdmin)