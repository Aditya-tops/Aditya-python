from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the homepage!")

def about(request):
    return HttpResponse("This is the about page!")
