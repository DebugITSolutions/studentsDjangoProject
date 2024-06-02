from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lesson, Student, Grade


@receiver(post_save, sender=Lesson)
def create_default_grades(sender, instance, created, **kwargs):
    if created:
        students = Student.objects.all()
        for student in students:
            Grade.objects.create(student=student, lesson=instance)
