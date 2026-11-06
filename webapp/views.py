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


class TodoCreateView(TemplateView):
    template_name = 'create_todo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('todo_view', pk=todo.pk)

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


class TodoUpdateView(TemplateView):
    template_name = 'todo_update.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        todo = get_object_or_404(Todo, pk=pk)
        form = TodoForm(initial={'summary': todo.summary, 'description': todo.description, 'status': todo.status, 'type': todo.type})
        return self.render_to_response({'form': form, 'todo': todo})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        todo = get_object_or_404(Todo, pk=pk)
        form = TodoForm(data=request.POST)

        if form.is_valid():
            todo.summary = form.cleaned_data['summary']
            todo.description = form.cleaned_data['description']
            todo.status = form.cleaned_data['status']
            todo.type = form.cleaned_data['type']
            todo.save()
            return redirect('todo_detail', pk=todo.pk)

        return self.render_to_response({'form': form, 'todo': todo})


class TodoDeleteView(TemplateView):
    template_name = 'delete_todo.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        todo = get_object_or_404(Todo, pk=pk)
        return self.render_to_response({'todo': todo})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return redirect('todo_list')