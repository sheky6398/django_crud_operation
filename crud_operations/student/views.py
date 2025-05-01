from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.http import HttpResponseRedirect



def crud_operations(request):
    students = Student.objects.all()

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return redirect('/crud/student')  # avoids resubmission on refresh
    else:
        student_form = StudentForm()

    context = {
        "students": students,
        "student_form": student_form
    }
    return render(request, 'crud.html', context)


def delete_student_record(request, id):
    if request.method == 'POST':
        student_instance = get_object_or_404(Student, pk=id)
        print(f'\n\n {student_instance = }  \n')
        student_instance.delete()
        return redirect('/crud/student')
    

def update_student_record(request, id):
    pi = Student.objects.get(pk=id)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=pi)    
        if student_form.is_valid():
            student_form.save()
            return redirect('/crud/student')  # avoids resubmission on refresh
    else:
        student_form = StudentForm(instance=pi)
    context = {
        "student": student_form,
    }
    print(f'\n update student record {id = }   \n\n')
    return render(request, 'update_student_data.html', context)




