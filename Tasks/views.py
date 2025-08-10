from rest_framework.viewsets import ModelViewSet
from Tasks.serializers import TaskSerializer, CategorySerializer
from .models import Category, Task
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TasksViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get_serializer_context(self):
        return {'user': self.request.user}


class CategoryViewSet(ModelViewSet):
    serializer_class =  CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return Category.objects.prefetch_related('tasks').filter(user=self.request.user)

