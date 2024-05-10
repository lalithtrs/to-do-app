from django.shortcuts import render, redirect
from django.views.generic import ListView
# Create your views here.
from .models import Todo
from .forms import TodoForms

# class TodoListView(ListView):
#     model = Todo

# def save_todo(request):


def todo_list(request):
    todos = Todo.objects.all()
    if(request.method == 'POST'):
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TodoForms()
    return render(request, 'todo/todo_list.html', {'object_list': todos, 'form': form})


def delete_todo(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('/')


def active_cross(request, id):
    print('working')
    task = Todo.objects.get(id=id)
    task.completed = not task.completed
    task.save()
    return redirect('/')
