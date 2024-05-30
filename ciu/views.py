from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully!')
            return redirect('student_form')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = StudentForm()
    return render(request, 'ciu/student_form.html', {'form': form})
