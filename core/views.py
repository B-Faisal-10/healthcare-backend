from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import *

# Register API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Patient CRUD
class PatientListCreate(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

# Doctor CRUD
class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Mapping
class MappingListCreate(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MappingDetail(generics.RetrieveDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorMappingsByPatient(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient__id=patient_id)


