from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Choices
COUNTRY_CHOICES = [
    ('IN', 'India'),
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
]

STATE_CHOICES = [
    ('KA', 'Karnataka'),
    ('MH', 'Maharashtra'),
    ('DL', 'Delhi'),
    ('TN', 'Tamil Nadu'),
    ('GJ', 'Gujarat'),
]

GRADE_CHOICES = [
    ('A+', 'Excellent'),
    ('A', 'Very Good'),
    ('B', 'Good'),
    ('C', 'Average'),
    ('D', 'Below Average'),
    ('F', 'Fail'),
]

ACTIVITY_CHOICES = [
    ('sports', 'Sports'),
    ('music', 'Music'),
    ('dance', 'Dance'),
    ('drama', 'Drama'),
    ('nss', 'NSS'),
    ('scouts', 'Scouts & Guides'),
    ('art', 'Art & Craft'),
    ('coding', 'Coding Club'),
    ('literature', 'Literary Club'),
]

class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    std_class = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    email = models.EmailField(null=False, unique=True, default='')
    phone_number = PhoneNumberField(null=False, blank=False,unique=True,default='+911234567890')
    
    class Meta:
        db_table = "Students"

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Class {self.std_class}) (email{self.email})"
    
    

class ExtraCurricular(models.Model):
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    activities = models.CharField(max_length=15, choices=ACTIVITY_CHOICES)
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name="activities") # for reverse look up 

    class Meta:
        db_table = "ExtraCurricular"

    def __str__(self):
        return f"{self.activities} ({self.get_grade_display()}) - {self.student.first_name}"

class Address(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE, related_name="address")
    house_no = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='IN')
    postal_code = models.CharField(max_length=10)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = "Address"

    def __str__(self):
        return f"{self.house_no}, {self.street}, {self.city}, {self.get_state_display()}, {self.get_country_display()}"
