# serializers.py
from rest_framework import serializers

from .models import Professor
from .models import Subject
from .models import Student



class ProfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = ('id','name', 'rating')

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('id','name', 'year', 'semester', 'professor')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'email')