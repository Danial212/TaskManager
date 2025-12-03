from rest_framework import fields, serializers
from .models import Category, Task



class TaskSerializer(serializers.ModelSerializer):
    #   Filter categories that belong to the authenticated user
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.none()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'user' in self.context:
            self.fields['category'].queryset =  Category.objects.filter(
                user=self.context['user'])
    
    #   Automaticly assign the authenticated user, for the new task
    def create(self, validated_data):
        return Task.objects.create(**validated_data, user=self.context['user'])

    class Meta:
        model = Task
        fields = ['id', 'title','description', 'category', 
                  'has_reminder','reminder', 'status','proirity']

class SimpleTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'url', 'title','description','has_reminder',
                  'reminder', 'status','proirity']

class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = obj.tasks.filter(user=self.context['user'])
        return SimpleTaskSerializer(tasks, many=True, context = {'request': self.context['request']}).data

    #   Automaticly assign the authenticated user, for the new category    
    def create(self, validated_data):
        return Category.objects.create(**validated_data, user=self.context['user'])

    class Meta:
        model = Category
        fields = '__all__'
        
