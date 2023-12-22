from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import ToDo

# Create your views here.


def index(request):
    todo_list = ToDo.objects.all()
    return render(request, 'base.html', {"todo_list":todo_list})

@require_http_methods(["POST"])
def add(request):
    task = request.POST["task"]
    add = ToDo(task=task, complete=False)
    add.save()
    return redirect("index")

def update(request, todo_id):
    task = ToDo.objects.get(id=todo_id)
    task.complete = not task.complete
    task.save()
    return redirect("index")

def delete(request, todo_id):
    task = ToDo.objects.get(id=todo_id)
    task.delete()
    return redirect("index")
    
        