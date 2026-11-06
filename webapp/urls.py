from django.urls import path
from webapp.views import IndexView, TodoCreateView, TodoView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='todo_list'),
    path('todo/add/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/', TodoView.as_view(), name='todo_view'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
]