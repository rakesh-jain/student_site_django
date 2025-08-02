from django.urls import path, include
from student_site import views
from rest_framework.routers import DefaultRouter


# generic api 
# urlpatterns =[
#     path('students/',views.StudentListApiView.as_view(),name="students"),
#     path('students/<int:pk>/',views.StudentDetailsView.as_view(),name ="student-details"),
    
#     path('addresses/',views.AddressListApiView.as_view(),name="addresses-list"),
#     path('addresses/<int:pk>/',views.AddressDetailView.as_view(),name="address-details"),
    
#     path('activities/', views.ExraCurriCularApiView.as_view(), name='activity-list'),
#     path('activities/<int:pk>/', views.ExtraCurricularDetailView.as_view(), name='activity-detail'),
# ]

# for APIView 

# urlpatterns =[
#     path('students/',views.StudentApiView.as_view(),name ="students"),
#     path('students/<int:pk>/', views.StudentDetailAPIView.as_view(),name="student-details"),
    
#     path('address/',views.AddressApiView.as_view(),name = "address"),
#     path('address/<int:student_id>/',views.AddressDeailApiView.as_view(),name = "address-detail"),
    
#     path('activities/',views.ExtraCurricularAPIView.as_view(),name = "activities"),
#     path('activities/<int:student_id>/<int:id>/',views.ExtraCurricularDetailedView.as_view(),name = "activities-detail")
# ]

# for viewSet.ModelViewSet

router = DefaultRouter()

router.register('students',views.StudentViewSet)
router.register('address',views.AddressViewSet)
router.register('activities',views.ExtraCurricularViewSet)

urlpatterns = [
    path('',include(router.urls))
]