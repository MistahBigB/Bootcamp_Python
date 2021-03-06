from rest_framework import viewsets

from exercises import models
from .serializers import ExerciseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = models.Exercise.objects.all()
    serializer_class = ExerciseSerializer