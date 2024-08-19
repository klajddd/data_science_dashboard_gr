# questions/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
from .code_executor import execute_python_code

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=True, methods=['post'])
    def submit_code(self, request, pk=None):
        question = self.get_object()
        user_code = request.data.get('code', '')
        
        if not user_code:
            return Response({'error': 'No code provided'}, status=status.HTTP_400_BAD_REQUEST)

        results = execute_python_code(user_code, question.test_cases)
        return Response(results)