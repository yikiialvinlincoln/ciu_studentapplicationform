from datetime import date
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if not date_of_birth:
            raise forms.ValidationError("Date of Birth is required.")
        
        today = date.today()
        if date_of_birth == today:
            raise forms.ValidationError("Date of Birth can't be the same as the date of application.")
        
        if (today - date_of_birth).days < 6570:  # 6570 days is approximately 18 years
            raise forms.ValidationError("Applicants must be at least 18 years old.")
        
        return date_of_birth
