from django.http import HttpResponse


def hello(request):
    print("hello world")
    return HttpResponse("Hello India")
