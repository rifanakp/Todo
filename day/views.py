from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import Todoform
from . models import Todo
def index(request):
    todo=Todo.objects.all()
    form=Todoform()
    if request.method=='POST':
        form=Todoform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Todo Success</h1>")
    context = {
        "form":form,
        "todo":todo
    }
    return render(request,"index.html",context)
def update(request,id):
    todo = Todo.objects.get(id=id)
    form = Todoform(instance=todo)
    if request.method=='POST':
        form=Todoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Updated Success</h1>")
    context = {
        "form":form
    }
    return render(request,"update.html",context) 
def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponse("<h1>Deleted Success</h1>")
    return render(request,"index.html") 