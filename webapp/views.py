from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import TodoForm
from  webapp.models import Todo
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context


class TodoView(TemplateView):
    template_name = 'todo_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        context['todo'] = Todo.objects.get(pk=pk)
        return context


def todo_create_view(request):

    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'create_todo.html', {'form': form})
    elif request.method == 'POST':
        form = TodoForm(data= request.POST)
        if form.is_valid():
            task = form.cleaned_data.get('task')
            deadline = form.cleaned_data.get('deadline')
            status = form.cleaned_data.get('status')
            todo = Todo.objects.create(task=task, deadline=deadline, status=status)
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, 'create_todo.html', {'form': form})


def todo_delete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_todo.html', {'todo': todo})
    elif request.method == "POST":
        todo.delete()
        return redirect('todo_list')