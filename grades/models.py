from django.db import models
from django.core.exceptions import ValidationError


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    attendance_score = models.PositiveSmallIntegerField(default=0)
    activity_score = models.PositiveSmallIntegerField(default=0)
    presentation_score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('student', 'lesson')

    def clean(self):
        if not (0 <= self.attendance_score <= 1):
            raise ValidationError('Attendance score must be between 0 and 1.')
        if not (0 <= self.activity_score <= 4):
            raise ValidationError('Activity score must be between 0 and 4.')
        if not (0 <= self.presentation_score <= 4):
            raise ValidationError('Presentation score must be between 0 and 4.')
        if self.total_score() > 5:
            raise ValidationError('Total score cannot exceed 5.')

    def total_score(self):
        return self.attendance_score + self.activity_score + self.presentation_score

    def __str__(self):
        return f"{self.student} - {self.lesson}: {self.total_score()}"
