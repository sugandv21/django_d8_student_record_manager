from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
