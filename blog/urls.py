# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('professor', views.ProfViewSet)
# router.register('subject', views.SubjectViewSet)
# router.register('student', views.StudentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.List, name='list'),
    path('ratings/', views.Ratings, name='ratings')
]