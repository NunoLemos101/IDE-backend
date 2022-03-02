from django.shortcuts import render

def index(request):
    print(request.path)
    return render(request, "filesystem/index.html")
