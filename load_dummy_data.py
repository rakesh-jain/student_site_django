import os
import django
import random
from faker import Faker

# Setup Django
os.environ.setdefault("student_site", "myproject.settings")  # change to your project name
django.setup()

from student_site.models import Students, ExtraCurricular, Address

fake = Faker('en_IN')

ACTIVITIES = ['sports', 'music', 'dance', 'drama', 'nss', 'scouts', 'art', 'coding', 'literature']
GRADES = ['A+', 'A', 'B', 'C']
STATES = ['KA', 'MH', 'DL', 'TN', 'GJ']
COUNTRIES = ['IN', 'US', 'UK', 'CA', 'AU']

def create_dummy_data(count=50):
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.unique.email()
        phone_number = f"+91{fake.random_number(digits=10)}"
        std_class = random.randint(1, 12)

        student = Students.objects.create(
            first_name=first_name,
            last_name=last_name,
            std_class=std_class,
            email=email,
            phone_number=phone_number
        )

        # Add 1–3 activities
        for _ in range(random.randint(1, 3)):
            ExtraCurricular.objects.create(
                student=student,
                activities=random.choice(ACTIVITIES),
                grade=random.choice(GRADES)
            )

        # Address
        Address.objects.create(
            student=student,
            house_no=fake.building_number(),
            street=fake.street_name(),
            city=fake.city(),
            state=random.choice(STATES),
            country=random.choice(COUNTRIES),
            postal_code=fake.postcode(),
            landmark = fake.company() + " Landmark"
        )

    

if __name__ == "__main__":
    create_dummy_data(50)
