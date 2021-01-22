from django.shortcuts import render, HttpResponse
from .models import Todo

def homepage(request):
    return render(request, "index.htm")

def test(request):
    todo_list = Todo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def go(request):
    return render(request, "go.htm")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3" )

