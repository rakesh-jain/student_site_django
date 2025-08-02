from rest_framework import generics
from student_site.models import Students,Address,ExtraCurricular
from student_site.serializers.student_serializer import StudentSerializer,AddressSerializer,ExtraCurricularSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
# Create your views here.
# creating using the generics 
# class StudentListApiView(generics.ListAPIView):
#     queryset  = Students.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetailsView(generics.RetrieveDestroyAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class AddressListApiView(generics.ListAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

# class AddressDetailView(generics.RetrieveDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer

# class ExraCurriCularApiView(generics.ListAPIView):
#     queryset = ExtraCurricular.objects.all()
#     serializer_class = ExtraCurricularSerializer

# class ExtraCurricularDetailView(generics.RetrieveDestroyAPIView):
#     queryset = ExtraCurricular.objects.all()
#     serializer_class = ExtraCurricularSerializer

# created using the apiview 

# class StudentApiView(APIView):
#     def get(self,request):
#         students = Students.objects.all()
#         serializer = StudentSerializer(students,many= True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class StudentDetailAPIView(APIView):
#     def get_object(self,pk):
#         return get_object_or_404(Students,pk=pk)
    
#     def get(self,request,pk):
#         student = self.get_object(pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
     
#     def put(self,request,pk):
#         student = self.get_object(pk)
#         serilalizer = StudentSerializer(student, data = request.data)
#         if serilalizer.is_valid():
#             serilalizer.save()
#             return Response(serilalizer.data)
#         return Response(serilalizer.errors,status= status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         student = self.get_object(pk)
#         student.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
        
        
# class AddressApiView(APIView):
#     def get(self,request):
#         address = Address.objects.all()
#         serializer = AddressSerializer(address,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = AddressSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        

# class AddressDeailApiView(APIView):
#     def get_object(self, student_id):
#         return get_object_or_404(Address,student_id=student_id)
    
#     def get(self,request,student_id):
#         address = self.get_object(student_id)
#         serializer = AddressSerializer(address)
#         return Response(serializer.data)
    
#     def put(self,request,student_id):
#         address = self.get_object(student_id)
#         serializer = AddressSerializer(address,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,student_id):
#         address = self.get_object(student_id)
#         address_deleted = address.delete()
#         Response({AddressSerializer(address_deleted).data},status=status.HTTP_200_OK)           

# class  ExtraCurricularAPIView(APIView):
#     def get(self,request):
#         extraCurricular = ExtraCurricular.objects.all()
#         serilaizer = ExtraCurricularSerializer(extraCurricular,many=True)
#         return Response(serilaizer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         extracurricular_ser = ExtraCurricularSerializer(data = request.data )
#         if extracurricular_ser.is_valid():
#             extracurricular_ser.save()
#             return Response(extracurricular_ser.data,status = status.HTTP_201_CREATED)
#         return Response(extracurricular_ser.errors,status=status.HTTP_400_BAD_REQUEST)

# class  ExtraCurricularDetailedView(APIView):
#     def get_object(self,student_id):
#         return get_list_or_404(ExtraCurricular,student_id=student_id)
    
#     def get(self,request,student_id):
#         activities_data = self.get_object(student_id)
#         serilaizer = ExtraCurricularSerializer(activities_data,many = True)
#         return Response(serilaizer.data,status=status.HTTP_200_OK)
    
#     def put(self,request, student_id):
#         activity = self.get(student_id)
#         serializer = ExtraCurricularSerializer(activity,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
#     def get_activity_by_id(self,student_id,id):
#         return get_object_or_404(ExtraCurricular,id = id,student__student_id=student_id)
        
#     def delete(self,request,student_id,id):
#         try:
#             activity = self.get_activity_by_id(student_id,id)
#             activity.delete()
#             return Response({"message": "Activity deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
#         except ExtraCurricular.DoesNotExist:
#             return Response({"error": "Activity not found for this student."}, status=status.HTTP_404_NOT_FOUND) 
        
    
# viewset 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().select_related('address').prefetch_related('activities')
    serializer_class = StudentSerializer
    # parser_classes = [JSONParser]  default it json we can specify the parse class 
    from rest_framework.parsers import FileUploadParser,MultiPartParser
    parser_classes = [FileUploadParser] # it tells the request allows only the file content 
    parser_classes  = [MultiPartParser] # multi part parser to process the html type docs 
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        
        return queryset
    
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class ExtraCurricularViewSet(viewsets.ModelViewSet):
    queryset = ExtraCurricular.objects.all()
    serializer_class = ExtraCurricularSerializer