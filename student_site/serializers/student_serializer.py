from rest_framework import serializers
from myenv.myproject.student_site.models.models import Students,ExtraCurricular,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['student']
        
class ExtraCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCurricular
        exclude = ['student']
        
class StudentSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    activities = ExtraCurricularSerializer(required=False, many=True)

    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        activity_data = validated_data.pop('activities', [])

        # Create the student first
        student = Students.objects.create(**validated_data)

        # Create and link address if provided
        if address_data:
            Address.objects.create(student=student, **address_data)

        # Create each activity and link to student
        for activity in activity_data:
            ExtraCurricular.objects.create(student=student, **activity)

        return student

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        activity_data = validated_data.pop('activities', None)

        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

       
        if address_data:
            if hasattr(instance, 'address'):
                for attr, value in address_data.items():
                    setattr(instance.address, attr, value)
                instance.address.save()
            else:
                Address.objects.create(student=instance, **address_data)

       
        if activity_data is not None:
            instance.activities.all().delete()
            for activity in activity_data:
                ExtraCurricular.objects.create(student=instance, **activity)

        return instance

            

