from django.shortcuts import render, get_object_or_404
from .models import Lesson, Grade, Student
from django.db.models import Sum, F


def index(request):
    students = Student.objects.all().annotate(
        total_score=Sum(F('grade__attendance_score') + F('grade__activity_score') + F('grade__presentation_score'))
    ).order_by('-total_score')

    context = {
        'students': students
    }
    return render(request, 'index.html', context)


def student_dashboard(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    grades = Grade.objects.filter(student=student).select_related('lesson')

    total_attendance_score = grades.aggregate(Sum('attendance_score'))['attendance_score__sum'] or 0
    total_activity_score = grades.aggregate(Sum('activity_score'))['activity_score__sum'] or 0
    total_presentation_score = grades.aggregate(Sum('presentation_score'))['presentation_score__sum'] or 0

    context = {
        'student': student,
        'grades': grades,
        'total_attendance_score': total_attendance_score,
        'total_activity_score': total_activity_score,
        'total_presentation_score': total_presentation_score,
    }
    return render(request, 'student_dashboard.html', context)


def lessons_list(request):
    all_lessons = Lesson.objects.all().order_by('date')

    context = {
        'all_lessons': all_lessons,
    }
    return render(request, 'lessons_list.html', context)


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    grades = Grade.objects.filter(lesson=lesson).select_related('student')

    sorted_grades = sorted(grades, key=lambda g: g.total_score(), reverse=True)

    context = {
        'lesson': lesson,
        'grades': sorted_grades
    }
    return render(request, 'lesson_detail.html', context)
