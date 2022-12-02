from django.shortcuts import render, redirect

from ToDoApp.forms import TaskForm
from ToDoApp.models import Todo


# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add(request):
    form = TaskForm(request.POST or None, auto_id=False)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form}
    return render(request, 'add.html', context)


def update(request, task_id):
    task = Todo.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update.html', {'form': form})


def delete(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect('index')


def search(request):
    search_term = request.GET.get('search') or ''
    todos = Todo.objects.filter(task__icontains=search_term)
    context = {'tasks': todos}
    return render(request, 'index.html', context)
