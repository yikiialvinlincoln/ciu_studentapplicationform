from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'course', 'entry_scheme', 'intake', 'sponsorship', 'gender', 'date_of_birth', 'residence']
        
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3 or len(first_name) > 50:
            raise forms.ValidationError("First name must be between 3 and 50 characters.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3 or len(last_name) > 50:
            raise forms.ValidationError("Last name must be between 3 and 50 characters.")
        return last_name
    
    def clean_residence(self):
        residence = self.cleaned_data.get('residence')
        if len(residence) < 2 or len(residence) > 50:
            raise forms.ValidationError("Residence must be between 2 and 50 characters.")
        return residence
