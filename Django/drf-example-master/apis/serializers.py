from rest_framework import serializers
from students import models

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'muscle_group',
            'ex_type',
            'equipment',
            'description',
            'youtube',
            'img'
        )
        model = models.Exercise