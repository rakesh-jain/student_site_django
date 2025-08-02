import os
import django
from django.db.models import Q,Count,Avg

# Set the settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # replace 'myproject' with your project name
django.setup()

# Now you can import your models
from student_site.models import Students, Address, ExtraCurricular

def get_all_records():
    student_data = Students.objects.all()
    for i in student_data:
        print(i)

def get_by_id():
    student = Students.objects.get(student_id=1)
    print(student)
    
def filter_data():
    student = Students.objects.filter(std_class = 9)
    for i in student:
        print(i)

def filter_data_count():
    student_count = Students.objects.filter(std_class = 9).count()
    print(student_count)

def filter_with_exclude():
    students = Students.objects.filter(std_class = 8).exclude()

def filter_data_with_Q():
    students = Students.objects.filter(Q(std_class = 8)| Q(std_class = 9))
    print(students)
def order_by():
    students = Students.objects.order_by('-std_class')
    for i in students:
        print(i)
def raw_data():
    student_list = Students.objects.raw('SELECT * FROM Students WHERE last_name = %s', ['jain'])
    for student in student_list:
        print(f"{student.first_name} {student.last_name} (Class {student.std_class})")

def onetoone_fetch():
    student = Students.objects.get(last_name = 'Jain')
    print(student.address)
    
def fetchActivity():
    student = Students.objects.get(last_name = 'Jain')
    print(student.activities.all())

def annotate_example():
    student = Students.objects.annotate(count_of_activities= Count('activities'))
    for i in student:
        print(i.first_name,i.count_of_activities)
        
def a_plus_students():
    students = Students.objects.filter(activities__grade ='A+')
    for s in students:
        print(s)
def get_rakeshData():
    student = Students.objects.get(last_name = 'Jain')
    activity = student.activities.all()
    for act in activity:
        print(act)

if __name__ == "__main__":
    get_rakeshData()
    
    