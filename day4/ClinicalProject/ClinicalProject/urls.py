from django.contrib import admin  # Add this line to import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Now the 'admin' is correctly defined
    path('doctors/', include('DoctorApp.urls')),
    path('patients/', include('PatientApp.urls')),
]