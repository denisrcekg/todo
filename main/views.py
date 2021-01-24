from django.shortcuts import render, HttpResponse
from .models import Todo
from .models import Bookstore

def homepage(request):
    return render(request, "index.htm")

def todo(request):
    todo_list = Todo.objects.all()
    return render(request, "todo.html", {"todo_list": todo_list})

def go(request):
    return render(request, "go.htm")

def second(request):
    return HttpResponse("test 2 page")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = Todo(text=text)
    todo.save()
    return redirect(todo)


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect(todo)


def mark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(todo)


def close_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(todo)

def third(request):
    return HttpResponse("This is page test3" )

def bookstore(request):
    books_list = Bookstore.objects.all()
    return render(request, "bookstore.htm", {"books_list": books_list})
