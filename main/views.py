from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("Hello world!")

def test(request):
    return render(request, "test.html")

def go(request):
    return render(request, "go.htm")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3" )

