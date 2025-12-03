from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Tasks import views


router = DefaultRouter()
router.register('tasks', views.TasksViewSet ,basename='task')
router.register('categories', views.CategoryViewSet ,basename='category')

urlpatterns = [
    path('', include(router.urls))
]