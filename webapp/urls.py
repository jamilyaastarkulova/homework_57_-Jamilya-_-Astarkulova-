from django.urls import path
from webapp.views import IndexView, todo_create_view, TodoView, todo_delete_view

urlpatterns = [
    path('', IndexView.as_view(), name='todo_list'),
    path('todo/add/', todo_create_view, name='todo_create'),
    path('todo/<int:pk>/', TodoView.as_view(), name='todo_view'),
    path('todo/<int:pk>/delete/', todo_delete_view, name='todo_delete'),
]