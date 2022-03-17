from rest_framework import viewsets

from .serializers import ProfSerializer
from .serializers import SubjectSerializer
from .serializers import StudentSerializer

from .models import Professor
from .models import Subject
from .models import Student


class ProfViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all().order_by('id')
    serializer_class = ProfSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer