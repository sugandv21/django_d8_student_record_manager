from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

# Home view
def home(request):
    return render(request, "students/layout/home.html")


# List all students
class StudentListView(ListView):
    model = Student
    template_name = "students/layout/student_list.html"
    context_object_name = "students"
    ordering = ['name']


# Show student detail
class StudentDetailView(DetailView):
    model = Student
    template_name = "students/layout/student_detail.html"
    context_object_name = "student"


# Register new student
class StudentCreateView(CreateView):
    model = Student
    template_name = "students/layout/student_form.html"
    fields = ['name', 'roll_no', 'course', 'age']
    success_url = reverse_lazy('student-list')  # redirect to list after creation

    def form_valid(self, form):
        messages.success(self.request, "Student registered successfully! 🎉")
        return super().form_valid(form)


# Edit student data
class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/layout/student_form.html"
    fields = ['name', 'roll_no', 'course', 'age']
    success_url = reverse_lazy('student-list')

    def form_valid(self, form):
        messages.success(self.request, "Student details updated successfully! ✏️")
        return super().form_valid(form)


# Delete student
class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/layout/student_confirm_delete.html"
    success_url = reverse_lazy('student-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Student deleted successfully! 🗑️")
        return super().delete(request, *args, **kwargs)
