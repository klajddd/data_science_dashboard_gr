# questions/serializers.py
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'initial_code', 'test_cases', 'created_at', 'updated_at']