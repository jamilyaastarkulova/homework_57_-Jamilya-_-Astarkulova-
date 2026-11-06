from django.urls import path
from webapp.views import IndexView, todo_create_view, todo_view, todo_delete_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todo/add/', todo_create_view, name='todo_create'),
    path('todo/<int:pk>/', todo_view, name='todo_view'),
    path('todo/<int:pk>/delete/', todo_delete_view, name='todo_delete'),
]