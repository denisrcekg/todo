from django.shortcuts import render, HttpResponse, redirect
from .models import *


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "todo.html", {"todo_list": todo_list})


def second(request):
    return HttpResponse("test 2 page")


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.is_closed = False
    todo.save()
    return redirect(test)


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def todo(request, id):
    todo_object = ToDo.objects.get(id=id)
    return render(request, "todo_item.html", {"todo_object": todo_object})

def bookStore(request):
    book_list = BookStore.objects.all()
    return render(request, 'books.html', {"book_list": book_list})

def book_add(request):
    return render(request, 'books-add.html')

def add_book(request):
    form = request.POST
    bookstor = BookStore(
        title=form['book-title'],
        subtitle=form['book-subtitle'],
        description=form['book-description'],
        price=form['book-price'],
        genre=form['book-genre'],
        author=form['book-author'],
        year=form['book-year'])
    bookstor.save()

    return redirect(bookStore)

def delete_book(request, id):
    book = BookStore.objects.get(id=id)
    book.delete()

    return redirect(bookStore)


def favorite_book(request, id):
    book = BookStore.objects.get(id=id)
    if book.is_favorite:
        book.is_favorite = False
    else:
        book.is_favorite = True
    book.save()
    return redirect(bookStore)


def book_info(request, id):
    book = BookStore.objects.get(id=id)
    return render(request, 'book-detail.html', {'book': book})
