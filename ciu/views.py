from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been Submitted successfully!')  
            return redirect('student_form') 
    else:
        form = StudentForm()
    return render(request, 'ciu/student_form.html', {'form': form})

def success(request):
    return render(request, 'ciu/success.html')
