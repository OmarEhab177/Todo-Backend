from django.urls import path
from .views import TodoDetailView, TodoListCreateView


urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
]