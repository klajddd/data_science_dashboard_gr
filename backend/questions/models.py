from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    initial_code = models.TextField()
    test_cases = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title