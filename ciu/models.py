from django.db import models
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

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)
    entry_scheme = models.CharField(max_length=2, choices=ENTRY_SCHEME_CHOICES)
    intake = models.CharField(max_length=3, choices=INTAKE_CHOICES)
    sponsorship = models.CharField(max_length=3, choices=SPONSORSHIP_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    date_of_birth = models.DateField()
    residence = models.CharField(max_length=255)

    def clean(self):
        super().clean()
        date_of_birth = self.date_of_birth

        if not date_of_birth:
            raise ValidationError({"date_of_birth": "Date of Birth is required."})

        today = date.today()

        if date_of_birth == today:
            raise ValidationError({"date_of_birth": "Date of Birth can't be the same as the date of application."})

        if (today - date_of_birth).days < 6570:  # 6570 days is approximately 18 years
            raise ValidationError({"date_of_birth": "Applicants must be at least 18 years old."})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
