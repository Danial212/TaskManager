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
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data, user=self.context['user'])

    class Meta:
        model = Task
        fields = ['title','description', 'category', 
                  'has_reminder','reminder', 'status','color','proirity']

class SimpleTaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['url', 'title','description','has_reminder',
                  'reminder', 'status','proirity']

class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    def get_tasks(self, obj):
        tasks = obj.tasks.filter(user=self.context['request'].user)
        return SimpleTaskSerializer(tasks, many=True, context = {'request': self.context['request']}).data
    
    class Meta:
        model = Category
        fields = '__all__'
        
