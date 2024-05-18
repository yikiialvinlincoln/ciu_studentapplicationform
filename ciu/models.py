from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from datetime import date

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    COURSE_CHOICES = (
        ('CHS', 'Certificate in Health Science'),
        ('CAT', 'Certificate in Applied Technology'),
        ('BIT', 'Bachelor of Information Technology'),
        ('BBT', 'Bachelors in Business Technology'),
        ('MPH', 'Master of Public Health')
    )

    ENTRY_SCHEME_CHOICES = (
        ('AL', 'A-Level certificate'),
        ('AM', 'Adult/Mature Learning'),
        ('CE', 'Certificate'),
        ('DI', 'Diploma'),
        ('BA', 'Bachelors')
    )

    INTAKE_CHOICES = (
        ('JAN', 'January Intake'),
        ('MAY', 'May Intake'),
        ('AUG', 'August Intake')
    )

    SPONSORSHIP_CHOICES = (
        ('PR', 'Private'),
        ('GOV', 'Government'),
        ('BUR', 'Bursary')
    )

    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    entry_scheme = models.CharField(max_length=2, choices=ENTRY_SCHEME_CHOICES)
    intake = models.CharField(max_length=3, choices=INTAKE_CHOICES)
    sponsorship = models.CharField(max_length=3, choices=SPONSORSHIP_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    date_of_birth = models.DateField()

    residence = models.CharField(max_length=255, validators=[MinLengthValidator(2), MaxLengthValidator(50)])

    def clean(self):
        today = date.today()
        if self.date_of_birth == today:
            raise ValidationError("Date of Birth can't be the same as the date of application.")
        if (today - self.date_of_birth).days < 6570:  
            raise ValidationError("Applicants must be at least 18 years old.")
        
    def __str__(self):
        return self.first_name + " " + self.last_name    
