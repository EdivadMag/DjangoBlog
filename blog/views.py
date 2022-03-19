import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import HttpResponse

from .serializers import ProfSerializer
from .serializers import SubjectSerializer
from .serializers import StudentSerializer

from .models import Professor
from .models import Subject
from .models import Student
from .models import Rating


# class ProfViewSet(viewsets.ModelViewSet):
#     queryset = Professor.objects.all().order_by('id')
#     serializer_class = ProfSerializer

# class SubjectViewSet(viewsets.ModelViewSet):
#     queryset = Subject.objects.all().order_by('id')
#     serializer_class = SubjectSerializer

# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all().order_by('id')
#     serializer_class = StudentSerializer

@api_view(['GET'])
def List(request):
    subjects = Subject.objects.distinct().values('id','name','year','semester','professor')
    list=[]
    for sub in subjects:
        prof = Subject.objects.get(id=sub['id'])
        prof = prof.professor.all()
        x = ''
        for c in prof:
            x = x + str(c) + " "
        p = { "id": sub["id"], "name": sub["name"], "year": sub["year"],"semester": sub["semester"],"professor": x}
        list.append(p)
    
    
    result = {"subject list": list}
    response = HttpResponse (json.dumps(result))



    return HttpResponse(subjects[0])

@api_view(['GET'])
def Ratings(request):
    professors = Professor.objects.all().values('id','name')
    list=[]
    #subjects = Subject.objects.filter(professor='1IT')
    
    for prof in professors:
        subjects = Subject.objects.filter(professor=prof['id']).values('id','name','year','semester','professor')
        x=0
        y=0
        for sub in subjects:
            ratings = Rating.objects.filter(subject=sub['id']).values('rating')
            for rat in ratings:
                x=x+int(rat['rating'])
                y=y+1
        if y==0:
            p = {"subject": prof['name'], "rating": "no ratings"}
        else:
            p = {"subject": prof['name'], "rating": int(x/y)}
        list.append(p)
            
   # ratings = Rating.objects.filter(subject='IT4').values('rating')
    result = {"Professors list": list}
    response = HttpResponse (json.dumps(result))
    return HttpResponse(response)
